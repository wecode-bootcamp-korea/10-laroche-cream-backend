from django.views import View
from django.db.models import F, Prefetch
from django.http import JsonResponse
from django.db import connection, reset_queries

import requests
import json

from .models import (
    Menu,
    MainCategory,
    SubCategory,
    Product,
    ProductFlag,
    Description,
    Image,
    Component,
)

class MainView(View):
    def get(self, request):
        image_url = list(Image.objects.filter(product__productflag__best_flag = True).values('image_url'))
        images = []
        [images.append(i['image_url'].replace("[","").replace("]","").split(',')) for i in image_url]
        datas = list(Product.objects.filter(productflag__best_flag = True).values(
            "id",
            "product_line",
            "name",
            "sale_price",
            "price",
            "hash_tag",
        ))
        data = []
        [data.append({'product' : datas[i], 'images' : images[i]}) for i in range(len(datas))]
        return JsonResponse({'data': data}, status=200)

class AllItemView(View):
    def get(self, request):
        flag = list(ProductFlag.objects.values())
        flag_objects =[]
        for i in flag:
            flag_objects.append({
            'id'   : i['id'],
            'best' : i['best_flag'],
            'new'  : i['new_flag'],
            'gift' : i['gift_flag'],
            'sale' : i['sale_flag']
            })
        image_url = list(Image.objects.values('image_url'))
        images = []
        [images.append(i['image_url'].replace("[","").replace("]","").split(',')) for i in image_url]
        datas = list(Product.objects.values(
            "id",
            "product_line",
            "name",
            "sale_price",
            "price",
            "hash_tag",
        ))
        data = []
        for i in range(len(datas)):
            data.append({
            'product' : datas[i],
            'images'  : images[i],
            'best'    : flag_objects[i]['best'],
            'new'     : flag_objects[i]['new'],
            'gift'    : flag_objects[i]['gift'],
            'sale'    : flag_objects[i]['sale']
            })

        return JsonResponse({'data': data}, status=200)

class DetailItemView(View):
    def post(self, request):
        pid = json.loads(request.body)
        product = Product.objects.prefetch_related('productflag_set').select_related("description").prefetch_related("component_set").prefetch_related("image_set").get(id = pid['id'])
        img_set = product.image_set.all()[0].image_url
        img_url = img_set[:]
        img_url = img_url.replace("\"", '').replace("\"",'').replace('[','').replace(']','').replace("'","").replace(' ', '').split(',')
        del img_url[len(img_url)-1]

        product_object = {
            'id'          : pid['id'],
            'sale'        : product.productflag_set.all()[0].sale_flag,
            'best'        : product.productflag_set.all()[0].best_flag,
            'new'         : product.productflag_set.all()[0].new_flag,
            'gift'        : product.productflag_set.all()[0].gift_flag,
            'name'        : product.name,
            'product_line': product.product_line,
            'price'       : product.price,
            'sale_price'  : product.sale_price,
            'hash_tag'    : product.hash_tag,
            'description' : product.description.description,
            'component'   : product.component_set.all()[0].component,
            'image'       : img_url
        }

        return JsonResponse({'data': product_object}, status=200)

