from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from ..models.CartItem import CartItem


@login_required(login_url='login')
def delete_from_cart(request, id):
    item = get_object_or_404(CartItem, id=id)
    item.delete()
    return redirect('account')
