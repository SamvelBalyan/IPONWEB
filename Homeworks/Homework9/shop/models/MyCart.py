from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

from .Item import Item

class MyCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through='CartItem')

    # def __str__(self):
    #     return f"{self.user.username}'s cart"

class MyCartAdmin(admin.ModelAdmin):
    list_display = ['user']