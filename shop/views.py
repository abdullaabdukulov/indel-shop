from django.shortcuts import render
from .models import Category


def error_404_view(request, exception):
    return render(request, 'shop/404.html')

def shopmainview(requet, category_slug=None):
    categories = Category.objects.all()
    ctx = {'categories': categories}
    return render(requet, 'index.html', ctx)

def shopview(request):
    return render(request, 'shop.html')