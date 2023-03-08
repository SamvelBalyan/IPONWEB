from django.db import models
from django.contrib import admin

from .ItemCategory import ItemCategory
from .Store import Store 

class Item(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(null=True, blank=True, default='default_item.jpg', upload_to="items/")
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    price = models.FloatField(default=0, null=True)
    quantity = models.PositiveIntegerField(default=0)
    info = models.TextField(max_length=200)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture', 'category', 'price', 'quantity', 'info', 'store']
    
    class Meta:
        ordering=["quantity"]