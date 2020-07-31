from django.urls import path
from .views import ProductDetailTagView

urlpatterns = [
    path('/tag/<int:product_id>', ProductDetailTagView.as_view())
]
