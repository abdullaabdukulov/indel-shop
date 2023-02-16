from django.contrib import admin
from .models import Category, ProductsImage, ProductSizes, Product, ProductColor, Reviews
from django.db import models
from tinymce.widgets import TinyMCE


class ProductSizeModelAdmin(admin.TabularInline):
    model = ProductSizes
    raw_id_fields = ['product']


class ProdcutImageModelAdmin(admin.TabularInline):
    model = ProductsImage
    raw_id_fields = ['product']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProdcutColorModelAdmin(admin.TabularInline):
    model = ProductColor
    raw_id_fields = ['product']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProdcutImageModelAdmin, ProductSizeModelAdmin, ProdcutColorModelAdmin]


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['product', 'rating', 'created']
    list_filter = ['created']
