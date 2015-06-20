from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User


class Ecoxarxa(models.Model):
    name = models.CharField(max_length=100, help_text=_('Name'))
    url = models.URLField(help_text=_('web page'))


class Rebost(models.Model):
    name = models.CharField(max_length=100, help_text=_('Name'))
    ecoxarxa = models.ForeignKey(Ecoxarxa, related_name="rebosts")
    # group = models.OneToOneField(settings.AUTH_GROUP_MODEL, unique=True)


class Prosumer(models.Model):
    user = models.OneToOneField(User)
    ces_account = models.CharField(max_length=10, help_text=_('User account in IntegralCES'))


class Product(models.Model):
    name = models.CharField(max_length=100, help_text=_('Name'))
    price = models.DecimalField(
        decimal_places=2,
        max_digits=5)
    created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='products')
    producer = models.ForeignKey(Prosumer, related_name="products",
                                 related_query_name="products")
    stock = models.IntegerField()

    def is_available(self):
            return (self.stock >= 1)


class ExchangeDay(models.Model):
    '''
    One day for exchanging goods in the exchange group
    '''
    rebost = models.ForeignKey(Rebost, related_name="exchange")
    date = models.DateField()
    closing_date = models.IntegerField(
        help_text=_('How many days in aadvance the comanda closes'))


class Comanda(models.Model):
    '''
    A list of products to be delivered to the user on an ExchangeDay
    '''
    user = models.ForeignKey(Prosumer, related_name="comandes")
    products = models.ManyToManyField(Product, related_name="comandas")
    exchange_day = models.ForeignKey(ExchangeDay, related_name="comandas")
    #    status = TODO. must be something like 'pending, delivered, charged...'


class Payment(models.Model):
    '''
    Payment process for one Comanda
    '''
    comanda = models.ForeignKey(Comanda, related_name="payment")
    url = models.URLField(help_text=_('web page'))
