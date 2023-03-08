from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ..models.ItemCategory import ItemCategory
from ..models.StoreCategory import StoreCategory

@login_required(login_url='login')
def categories(request):
    item_cat = ItemCategory.objects.all()
    store_cat = StoreCategory.objects.all()

    return render(request, "categories.html", {"store_cat":store_cat, "item_cat":item_cat})
