from django.db import models
from django.contrib import admin

from .MyCart import MyCart
from .Item import Item

class CartItem(models.Model):
    my_cart = models.ForeignKey(MyCart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.item.name
    

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['my_cart', 'item', 'quantity']