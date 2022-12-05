from django.urls import path
from .views import shopmainview, shopview

urlpatterns = [
    path('', shopmainview, name='product_list_by'),
    path('shop/', shopview, name='product_details')
]   