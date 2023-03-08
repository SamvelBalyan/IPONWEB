from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from shop.models.Item import Item


@login_required(login_url='login')
def products(request):  
    
    products = Item.objects.all()    
    return render(request, 'home.html', {'products':products})