from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from products.models import Variation
from django.db.models.signals import pre_save, post_save, post_delete
from decimal import Decimal
# Create your models here.

class CartItem(models.Model):
    cart = models.ForeignKey("Carts")
    item = models.ForeignKey(Variation)
    quantity = models.PositiveIntegerField(default=1)
    line_item_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item.title

    def remove(self):
        return self.item.remove_from_cart()

def cart_item_pre_save_receiver(sender, instance, *args, **kwargs):
    qty = instance.quantity
    if qty >= 1:
        price = instance.item.get_price()
        line_item_total = Decimal(qty) * Decimal(price)
        instance.line_item_total = line_item_total

pre_save.connect(cart_item_pre_save_receiver, sender=CartItem)

def cart_item_post_save_receiver(sender, instance, *args, **kwargs):
    instance.cart.update_subtotal()

post_save.connect(cart_item_post_save_receiver, sender=CartItem)
post_delete.connect(cart_item_post_save_receiver, sender=CartItem)



class Carts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    items =  models.ManyToManyField(Variation, through=CartItem)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    tax_percentage = models.DecimalField(max_digits=10, decimal_places=5, default=0.085)
    subtotal = models.DecimalField(max_digits=50, decimal_places=2, default=250.00)
    tax_total = models.DecimalField(max_digits=50, decimal_places=2, default=250.00)
    total = models.DecimalField(max_digits=50, decimal_places=2, default=250.00)


    def __str__(self):
        return str(self.id)

    def update_subtotal(self):
        subtotal = 0
        items = self.cartitem_set.all()
        for item in items:
            subtotal += item.line_item_total
        self.subtotal = "%.2f" %(subtotal)
        self.save()


def do_tax_and_total_receiver(sender, instance, *args, **kwargs):
    subtotal = instance.subtotal
    tax_total = round(Decimal(subtotal) * Decimal(instance.tax_percentage),2)
    total = round(Decimal(tax_total) + Decimal(subtotal),2)
    instance.tax_total = "%.2f" %(tax_total)
    instance.total =  "%.2f" %(total)


pre_save.connect(do_tax_and_total_receiver, sender=Carts)
