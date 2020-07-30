from django.views import View
from django.http import (
    HttpResponse, 
    JsonResponse
)
from .models import ProductDetailTag


class ProductDetailTagView(View):
    def get(self, request, product_id):
        html_tag = ProductDetailTag.objects.get(id=product_id)
        print("html_tag : ", html_tag)
        
        data = {
            "id" : html_tag.id,
            "banner" : html_tag.banner,
            "detailView" : html_tag.productDetail,
            "detailMid" : html_tag.sec3,
            "detailPoint" : html_tag.sec5 ,
            "research" : html_tag.sec6 ,
            "PayInfo" : html_tag.purchaseView
        }

        return JsonResponse({'data': data})


