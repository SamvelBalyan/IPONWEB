from django.db import models
from django.contrib import admin


class ItemCategory(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(default='default_item.jpg',upload_to="item_category/")

    def __str__(self): return self.name


class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture']