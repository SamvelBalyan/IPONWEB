from django.urls import path

from .api.item import ItemView
from .api.mycart import MyCartView
from .api.cart_item import CartItemView
from .api.customer import CustomerView
from .api.item_category import ItemCategoryView
from .api.store import StoreView
from .api.store_category import StoreCategoryView
from .api.store_owner import StoreOwnerView

from .api.register import register
from .api.login import login
from .api.logout import logout
from .api.account import account
from .api.add_to_cart import add_to_cart
from .api.products import products
from .api.categories import categories
from .api.delete_from_cart import delete_from_cart
from .api.change_avatar import change_avatar