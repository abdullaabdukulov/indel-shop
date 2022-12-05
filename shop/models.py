from django.db import models
from django.urls import reverse

    
class Category(models.Model):
    name = models.CharField(max_length=200)
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