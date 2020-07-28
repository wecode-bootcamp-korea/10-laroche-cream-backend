from django.views import View
from django.db.models import F, Prefetch
from django.http import JsonResponse

from django.db import connection, reset_queries
import time
import functools

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
        data = models.Product.objects.filter(id<9).values(
            "prodct_line",
            "name",
            "sale_price",
            "price",
            "hash_tag",
        )
        return JsonResponse({'data':list(data), status=200})

class AllItemView(View):
    def get(self, request):
        data = modesl.Product.objects.all().values(
            "product_line",
            "name",
            "sale_price",
            "price",
            "hash_tag",

        )