from django.db import models


#Статус заказа
from products.models import Product

class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=0)
    is_active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name ="Статус"
        verbose_name_plural = 'Статусы заказа'

# Заказа
class Order(models.Model):
    total_price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    customer_name = models.CharField(max_length=128)
    stomer_email = models.EmailField(blank=True, null=True, default=0)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=48, blank=True, null=True, default=None)
    coments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return "Заказ %s %s" % (self.id, self.status)

    class Meta:
        verbose_name ="Заказ"
        verbose_name_plural = 'Заказы'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10,decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name ="Товар"
        verbose_name_plural = 'Товары'
