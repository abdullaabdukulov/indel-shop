from django.contrib import admin
from .models import Category, ProductsImage, ProductSizes, Product


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
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                       'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProdcutImageModelAdmin, ProductSizeModelAdmin]



