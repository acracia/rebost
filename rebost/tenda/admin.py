from django.contrib import admin
from django.conf import settings
from rebost.tenda.models import Product
from django.utils.translation import ugettext_lazy as _

class ProductAdmin(admin.ModelAdmin):
    list_filter = ['available']
    search_fields = ['name', 'producer', 'price']

admin.site.register(Product, ProductAdmin)

