from django.contrib import admin
from products.models import Product, ProductImage

class ProductImageline(admin.TabularInline):
    model = ProductImage
    extra = 0

#Запись в админку


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageline]

    class Meta:
        model = Product
admin.site.register(Product,ProductAdmin)

class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage

admin.site.register(ProductImage,ProductImageAdmin)
