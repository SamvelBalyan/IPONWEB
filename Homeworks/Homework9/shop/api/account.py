from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ..models.Customer import Customer
from ..models.MyCart import MyCart
from ..models.CartItem import CartItem



@login_required(login_url='login')
def account(request):
    customer = Customer.objects.get(user=request.user)
    cart = MyCart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(my_cart=cart)
    
    cont, total_cost=[], 0
    for item in cart_items:
        cont.append({'id':item.id,
                     'name':item.item.name,
                     'quantity':item.quantity,
                     'price':item.quantity*item.item.price})
        total_cost += item.quantity*item.item.price

    context = {'customer':customer, 'cart_items':cont, 'total_cost':total_cost}

    return render(request, 'account.html', context)
