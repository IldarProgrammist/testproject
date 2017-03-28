from django.shortcuts import render
from products.models import Product

from landing.forms import PersonForm


def landing(request):

    form = PersonForm(request.POST or None)

    if request.method =="POST" and form.is_valid():
        new_form = form.save()
    return render(request,'landing/landing.html', locals())


def home(request):
    products = Product.objects.filter(is_active=True)
    return render(request,'landing/home.html', locals())

