
from django.db import models


class Product(models.Model):

    customer_name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name ="Товар"
        verbose_name_plural = 'Товары'


class ProductImge(models.Model):

    product = models.ForeignKey(Product,blank=True, null=True, default=None )
    image = models.ImageField(upload_to='/product_images')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name ="Фоторафия"
        verbose_name_plural = 'Фотографии'
