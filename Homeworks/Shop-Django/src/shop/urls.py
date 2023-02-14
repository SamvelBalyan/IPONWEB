from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='home_n'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('item/<int:id>', views.show_item, name='item'),
    path('register/', views.register, name='register'),
    path('account/', views.account, name="account"),
    path('categories/', views.categories, name="categories_n"),
    path('delete_from_cart/<int:id>', views.delete_from_cart, name="delete_from_cart"),
    path('add_to_cart/<int:id>', views.add_to_cart, name="add_to_cart"),
    path('change_avatar/', views.change_avatar, name='change_avatar'),

    
]