from django.contrib import admin

from .models.StoreCategory import StoreCategory, StoreCategoryAdmin
from .models.ItemCategory import ItemCategory, ItemCategoryAdmin
from .models.Customer import Customer, CustomerAdmin
from .models.StoreOwner import StoreOwner, StoreOwnerAdmin
from .models.Store import Store, StoreAdmin
from .models.Item import Item, ItemAdmin
from .models.MyCart import MyCart, MyCartAdmin
from .models.CartItem import CartItem, CartItemAdmin

admin.site.register(StoreCategory, StoreCategoryAdmin)
admin.site.register(ItemCategory, ItemCategoryAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(StoreOwner, StoreOwnerAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(MyCart, MyCartAdmin)
