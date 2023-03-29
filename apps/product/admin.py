from django.contrib import admin
from .models import (
    Category, Promotion, PromotionCategory, Product, ProductItem,
    Variation, VariationOpinion, ProductConfigurations, Media
)


class VariationOpinionInline(admin.TabularInline):
    model = VariationOpinion


class VariationInline(admin.StackedInline):
    model = ProductConfigurations
    raw_id_fields = ['product_item']


class MediaInline(admin.TabularInline):
    model = Media
    raw_id_fields = ['product_item']


class ProductItemInline(admin.TabularInline):
    model = ProductItem
    raw_id_fields = ['product']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'background_image', 'parent']
    list_filter = ['parent']
    prepopulated_fields = {'slug': ['name', ]}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    inlines = [ProductItemInline, ]
    prepopulated_fields = {'slug': ['name']}


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'discount_rate', 'start_date', 'end_date', 'created_at']
    list_filter = ['start_date', 'end_date', 'discount_rate']
    search_fields = ('name', 'description',)


@admin.register(PromotionCategory)
class PromotionCategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'promotion']


@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'sku', 'qty_in_stock', 'price', 'created_at']
    inlines = [MediaInline, VariationInline]


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ['category', 'name']
    inlines = [VariationOpinionInline, ]


@admin.register(VariationOpinion)
class VariationOpinionAdmin(admin.ModelAdmin):
    list_display = ['variation', 'value']


@admin.register(ProductConfigurations)
class ProductConfigurationsAdmin(admin.ModelAdmin):
    list_display = ['product_item', 'product_opinion']
