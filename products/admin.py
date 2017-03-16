from django.contrib import admin
from .models import *
from landing.models import Person


# class PersonAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email']
#     list_filter = ['name']
#     search_fields = ['name']
#
#     class Meta:
#         model = Person
# admin.site.register(Person, PersonAdmin)

