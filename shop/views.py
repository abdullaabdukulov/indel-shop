from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Reviews
from .forms import ReviewsForm

def error_404_view(request, exception):
    return render(request, 'erorrs/404.html')

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


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    reviews = Reviews.objects.filter(product=id).order_by('-created').values()
    ctx = {'product': product, 'reviews': reviews}

    return render(request, 'product-single.html', ctx)


def add_review(request, id):
    product = get_object_or_404(Product, id=id, available=True)
    if request.method == 'POST':
        form = ReviewsForm(request.POST or None)
        if form.is_valid():
            data = Reviews(
                comment = request.POST.get('comment'),
                rating = request.POST.get('rating'),
                product = product
            )
            data.save()
            return redirect('shop:product_detail', product.id, product.slug)
    return redirect('shop:product_detail', product.id, product.slug)
            


        
