from django.contrib import admin
from .models import Advert


admin.site.register(Advert)

"""
from django.contrib import admin
from .models import Advert


class AdvertAdmin(admin.ModelAdmin):
    list_display = ['name',  'description', 'price',  'created', 'updated', 'seller']
    list_editable = [description', 'price']
    list_per_page = 20

admin.site.register(Product, ProductAdmin)
"""