from django.db import models
from django.contrib import admin

from .StoreOwner import StoreOwner
from .StoreCategory import StoreCategory


class Store(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(StoreOwner, on_delete=models.CASCADE)
    store_category = models.ForeignKey(StoreCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'store_category']
