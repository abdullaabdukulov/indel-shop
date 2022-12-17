from django.db import models
from django.urls import reverse
from colorfield.fields import ColorField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


    
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200,
                            unique=True)
    image = models.ImageField(upload_to='category/')
    description = models.TextField(max_length=400, default='')

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    product_front_image = models.ImageField(upload_to='products/%Y/%m/%d')
    description = models.TextField(max_length=400)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    statement = models.TextField()
    available = models.BooleanField(default=True)    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
           return reverse('shop:product_detail',
                          args=[self.id, self.slug])


class ProductsImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='images', verbose_name='product')
    image = models.ImageField(upload_to='products/%Y/%m/%d/product_images/', null=True, blank=True)
    
    class Meta:
        verbose_name = 'product image'
        verbose_name_plural = 'product images'
    
    def __str__(self):
        return self.product.name

class ProductSizes(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='sizes')
    size = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = 'product size'
        verbose_name_plural = 'product sizes'

    def __str__(self):
        return self.product.name

class ProductColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='color', blank=True, null=True)
    color = models.CharField(max_length=10)
    code = ColorField(default='#FF0000')
    

    class Meta:
        verbose_name = 'product color'
        verbose_name_plural = 'product colors'
    
    def __str__(self):
        return self.product.name

class Reviews(models.Model):
    content = models.TextField(max_length=400)
    rating = models.FloatField(default=5, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'product review'
        verbose_name_plural = 'product reviews'

    def __str__(self):
        return self.product.name
