from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    background_image = models.ImageField(upload_to='category', blank=True, null=True)

    def __str__(self):
        return self.name


class Promotion(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    discount_rate = models.FloatField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PromotionCategory(models.Model):
    category = models.ForeignKey(Category, related_name='promotion_categories', on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, related_name='promotion_categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.category.name


class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductItem(models.Model):
    product = models.ForeignKey(Product, related_name='product_items', on_delete=models.CASCADE)
    sku = models.CharField(max_length=250)
    qty_in_stock = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sku


class Variation(models.Model):
    category = models.ForeignKey(Category, related_name='category_variations', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class VariationOpinion(models.Model):
    variation = models.ForeignKey(Variation, related_name='variations', on_delete=models.CASCADE)
    value = models.CharField(max_length=250)

    def __str__(self):
        return self.value


class ProductConfigurations(models.Model):
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name='product_configurations')
    product_opinion = models.ForeignKey(VariationOpinion, on_delete=models.CASCADE, related_name='product_opinions')

    def __str__(self):
        return f"{self.product_item}, {self.product_opinion}"


class Media(models.Model):
    image = models.ImageField(upload_to='product_item/%Y/%m/%d')
    product_item = models.ForeignKey(ProductItem, related_name='media', on_delete=models.CASCADE)


