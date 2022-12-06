from django.shortcuts import render
from .models import Category, Product


def error_404_view(request, exception):
    return render(request, 'shop/404.html')

def shopmainview(requet, category_slug=None):
    categories = Category.objects.all()
    ctx = {'categories': categories}
    return render(requet, 'index.html', ctx)

def product_list(request):
    products = Product.objects.all()
    ctx = {'products': products}
    return render(request, 'shop.html', ctx)