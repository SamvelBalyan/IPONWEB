from django.contrib import admin

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