from django.urls import path
from .views import shopmainview, product_list, product_detail

urlpatterns = [
    path('', shopmainview, name='product_list_by'),
    path('category/<slug:category_slug>/', shopmainview,
         name='product_list_by_category'),
    path('product/', product_list, name='product_list'),
    path('product/<slug:product_slug>', product_detail, name='product_detail')
]   