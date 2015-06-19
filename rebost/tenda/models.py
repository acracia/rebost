from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class Ecoxarxa(models.Model):
    name = models.CharField(max_length=100, help_text=_('Name'))
    url = URLField(help_text=_('web page'))

class Rebost(models.Model):
    name = models.CharField(max_length=100, help_text=_('Name'))
    ecoxarxa = models.ForeignKey(Ecoxarxa, related_name="rebosts")

class Product(models.Model):
    name = models.CharField(max_length=100, help_text=_('Name'))
    price = models.DecimalField(
        decimal_places=2,
        max_digits=5))
    available = models.BooleanField(help_text=_('Available for next rebosts'))
    created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='products')
    producer = models.ForeignKey(Prosumer, related_name="products",
                                 related_query_name="products")

