from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    background_image = models.ImageField(upload_to='category')

    def __str__(self):
        return self.name


class Promotion(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    discount_rate = models.FloatField()
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField()


class PromotionCategory(models.Model):
    category = models.ForeignKey(Category, related_name='pr_category', on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, related_name='pr_promotion', on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='product/%Y/%m/%d')


class ProductItem(models.Model):
    product = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
    sku = models.CharField(max_length=250)
    qty_in_stock = models.IntegerField()
    price = models.IntegerField()


class Variation(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)


class VariationOpinion(models.Model):
    variation = models.ForeignKey(Variation, related_name='variation', on_delete=models.CASCADE)
    value = models.CharField(max_length=250)


class ProductConfigurations(models.Model):
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name='product_item')
    product_opinion = models.ForeignKey(VariationOpinion, on_delete=models.CASCADE, related_name='product_opinion')


class Media(models.Model):
    image = models.ImageField(upload_to='product_item/%Y/%m/%d')
    product_item = models.ForeignKey(ProductItem, related_name='product_item', on_delete=models.CASCADE)