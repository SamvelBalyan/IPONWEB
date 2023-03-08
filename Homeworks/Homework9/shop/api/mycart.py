import json
from django.views.generic import View
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from ..models.MyCart import MyCart
from ..models.Item import Item
from ..models.CartItem import CartItem
 
from ..utils import ok_status, data_status

class MyCartView(View):

    ###
    def get(self, request):
        my_carts = MyCart.objects.all()
        data = []
        for my_cart in my_carts:
            items = []
            for item in my_cart.items.all():
                items.append({
                    "name": item.name,
                    "id": item.id,
                })
            data.append({
                "id": my_cart.id,
                "items": items,
            })
        return data_status(data)
    
    ###
    @staticmethod
    def get_single(request, id):
        try:
            cart = MyCart.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        items=[]
        for item in cart.items.all():
                items.append({
                    "name": item.name,
                    "id": item.id,
                })

        return data_status({
            "id": cart.id,
            "items": items,
        })
    

    ###
    @staticmethod
    def post(request, id):

        item = Item.objects.get(id=id)
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

        return ok_status()


    ###
    @staticmethod
    def delete(request, id):

        item = CartItem.objects.get(my_cart=MyCart.objects.get(user=request.user), id=id)
        item.delete()

        return ok_status()
    

    ###
    @staticmethod
    def check_view(request, id):
        # print(f"### {request.method} ###")
        if request.method == "GET":
            print("###GET###")
            return MyCartView.get_single(request, id)
        if request.method == "POST":
            print("###POST###")
            return MyCartView.post(request, id)
        if request.method == "DELETE":
            print("###Delete###")
            return MyCartView.delete(request, id)