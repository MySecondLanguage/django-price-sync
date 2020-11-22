from django.contrib import admin
from price.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sku',
        'price',
        'extracted_price',
        'title',
        'url',
        'last_update',
    )
    
admin.site.register(Product, ProductAdmin)