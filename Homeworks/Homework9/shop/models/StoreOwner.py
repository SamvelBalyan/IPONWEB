from django.db import models
from django.contrib import admin

from django.contrib.auth.models import User

class StoreOwner(models.Model):
    
    avatar = models.ImageField(default='default_item.jpg', upload_to="store_owner/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registrated_at = models.DateTimeField(auto_now_add=True)


class StoreOwnerAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'registrated_at']
