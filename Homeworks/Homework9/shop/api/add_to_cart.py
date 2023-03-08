from __future__ import absolute_import

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ..models.Item import Item
from ..models.MyCart import MyCart
from ..models.CartItem import CartItem


@login_required(login_url='login')
def add_to_cart(request, id):

    item = Item.objects.get(id=id)
    print(item)
    cart, created = MyCart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(
        my_cart=cart,
        item=item
    )
    if not created:
        cart_item.quantity += 1
    else:
        cart_item.quantity = 1
    cart_item.save()
    cart.save()

    return render(request, 'add_to_cart.html', {})
