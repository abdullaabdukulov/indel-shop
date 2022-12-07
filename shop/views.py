from django.shortcuts import render, get_object_or_404
from .models import Category, Product, ProductSizes, ProductsImage
from . import services

def error_404_view(request, exception):
    return render(request, 'shop/404.html')

def shopmainview(request, category_slug=None):
    category, products = None, None
    categories = Category.objects.all()
    if category_slug:
        category  = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, available=True)
        ctx =  {
            'category': category,
            'products': products
        }
        return render(request, 'shop.html', ctx)
    ctx = {'categories': categories}
        
   
    return render(request, 'index.html', ctx)

def product_list(request):
    products = Product.objects.filter(available=True)
    ctx = {'products': products}
    return render(request, 'shop.html', ctx)


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug, available=True)
    ctx = {'product': product}
    return render(request, 'product-single.html', ctx)
