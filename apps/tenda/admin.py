from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    # list_filter = ['is_available']
    search_fields = ['name', 'producer', 'price']

admin.site.register(Product, ProductAdmin)
