from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default_item.jpg',upload_to="customer/")
    registrated_at = models.DateTimeField(auto_now_add=True)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'registrated_at']
