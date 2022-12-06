from django.urls import path
from .views import shopmainview, product_list

urlpatterns = [
    path('', shopmainview, name='product_list_by'),
    path('shop/', product_list, name='product_list'),
]   