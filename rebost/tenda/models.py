from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

# Create your models here.

class Ecoxarxa(models.Model):
    name = models.CharField(max_length=100, help_text=_('Name'))
    url = URLField(help_text=_('web page'))

class Rebost(models.Model):
    name = models.CharField(max_length=100, help_text=_('Name'))
    ecoxarxa = models.ForeignKey(Ecoxarxa, related_name="rebosts")
    group = models.OneToOneField(settings.AUTH_GROUP_MODEL, unique=True)

class Product(models.Model):
    name = models.CharField(max_length=100, help_text=_('Name'))
    price = models.DecimalField(
        decimal_places=2,
        max_digits=5))
    #available = models.BooleanField(help_text=_('Available for next rebosts'))
    created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='products')
    producer = models.ForeignKey(Prosumer, related_name="products",
                                 related_query_name="products")
    stock = models.IntegerField()
    def available():
            return ( self.stock <=1 )
class Prosumer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    ces_account = models.Charfield(help_text=_('User account in IntegralCES'))
    
class Exchange(models.Model):
    rebost = models.ForeignKey(Rebost, related_name="exchange")
    date = models.DateField()

class Comanda(models.Model):
    user = models.ForeignKey(Prosumer, related_name="comandes")
    products = models.ManyToManyField(Product, related_name="comandas")
    exchange = models.ForeignKey(Exchange, related_name="comandas")
    #    status = TODO. must be something like 'pending, delivered, charged...'


