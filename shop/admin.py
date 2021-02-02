from django.contrib import admin

from shop.models import Purchase, Item

admin.site.register(Item)
admin.site.register(Purchase)
