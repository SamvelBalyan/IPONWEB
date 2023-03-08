from django.db import models
from django.contrib import admin


class StoreCategory(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(default='default_item.jpg',upload_to="store_category/")

    def __str__(self):
        return self.name
    
class StoreCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture']