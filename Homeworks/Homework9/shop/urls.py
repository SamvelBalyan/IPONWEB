from .imports import *

urlpatterns = [
    path('', products, name='home_n'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

    path('items/<int:id>', ItemView.check_view, name='item'),
    path('items/', ItemView.as_view(), name='item'),

    path('customers/<int:id>', CustomerView.check_view, name='customer'),
    path('customers/', CustomerView.as_view(), name='customer'),

    path('item_categories/<int:id>', ItemCategoryView.check_view, name='item_categories'),
    path('item_categories/', ItemCategoryView.as_view(), name='item_category'),

    path('store_categories/<int:id>', StoreCategoryView.check_view, name='store_categories'),
    path('store_categories/', StoreCategoryView.as_view(), name='store_category'),

    path('carts/<int:id>/add_to_cart', MyCartView.check_view, name='add_to_cart'),
    path('carts/<int:id>/delete', MyCartView.check_view, name='delete'),
    path('carts/<int:id>', MyCartView.check_view, name='cart'),
    path('carts/', MyCartView.as_view(), name='cart'),

    path('stores/<int:id>', StoreView.check_view, name='store'),
    path('stores/', StoreView.as_view(), name='store'),

    path('register/', register, name='register'),
    path('account/', account, name="account"),
    path('categories/', categories, name="categories_n"),
    path('change_avatar/', change_avatar, name='change_avatar'),
]