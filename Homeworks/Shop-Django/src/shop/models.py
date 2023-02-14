from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class StoreCategory(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(default='default_item.jpg',upload_to="store_category/")

    def __str__(self): return self.name


class ItemCategory(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(default='default_item.jpg',upload_to="item_category/")

    def __str__(self): return self.name


class StoreOwner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default_item.jpg', upload_to="store_owner/")
    registrated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.user.username


class Store(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(StoreOwner, on_delete=models.CASCADE)
    store_category = models.ForeignKey(StoreCategory, on_delete=models.CASCADE)

    def __str__(self): return self.name


class Item(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(null=True, blank=True, default='default_item.jpg', upload_to="items/")
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    price = models.FloatField(default=0, null=True)
    quantity = models.PositiveIntegerField(default=0)
    info = models.TextField(max_length=200)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self): return f"{self.name}"


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, default='default-avatar.png',upload_to="customer/")
    registrated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.user.username



class MyCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through='CartItem')

    def __str__(self): 
        return f'MyCart: {self.id}'


class CartItem(models.Model):
    my_cart = models.ForeignKey(MyCart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.item.name} ({self.quantity})"
    
class StoreCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture']

class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'registrated_at']

class StoreOwnerAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'registrated_at']

class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'store_category']

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture', 'category', 'price', 'quantity', 'info', 'store']
    
    class Meta:
        ordering=["quantity"]

class MyBugAdmin(admin.ModelAdmin):
    list_display = ['user']

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['buy_time', 'customer']

# add to .gitignore
# migrations
# media folder
# .vscode
# .idea
