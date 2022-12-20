from django.urls import path
from .views import shopmainview, product_list, product_detail, add_review

app_name ='shop'

urlpatterns = [
    path('', shopmainview, name='home'),
    path('category/<slug:category_slug>/', shopmainview,
         name='product_list_by_category'),
    path('product/', product_list, name='product_list'),
    path('product/<int:id>/<slug:slug>', product_detail, name='product_detail'),
    path('product/add_review/<slug:id>/', add_review,name="add_review"),
]   