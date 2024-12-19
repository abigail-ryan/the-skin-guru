from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product, Category, Brand, SkinType

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    summernote_fields = ('description', 'key_ingredients', 'ingredients', 'how_to_use')
    list_display = (
        'name',
        'brand',
        'category',
        'price',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class SkinTypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(SkinType, SkinTypeAdmin)