from django.shortcuts import render
from products.models import Product, ProductImage

from landing.forms import PersonForm


def landing(request):

    form = PersonForm(request.POST or None)

    if request.method =="POST" and form.is_valid():
        new_form = form.save()
    return render(request,'landing/landing.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    return render(request,'landing/home.html', locals())

