import json

from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from ..models.CartItem import CartItem

from ..utils import data_status, ok_status

class CartItemView(View):
    
    def get(self, request):
        cart_items = CartItem.objects.all()
        data = []
        for cart_item in cart_items:
            data.append(
                {
                    "id": cart_item.id,
                    "item_id": cart_item.item.id,
                    "customer_id": cart_item.customer.id,
                    "quantity": cart_item.quantity,
                }
            )
        return data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        cart_item = CartItem.objects.create(
            item_id=data["item_id"], customer_id=data["customer_id"], quantity=data["quantity"]
        )
        cart_item.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return CartItemView.get_single(request, id)
        if request.method == "DELETE":
            return CartItemView.delete(request, id)
        if request.method == "PATCH":
            return CartItemView.edit(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            cart_item = CartItem.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return data_status(
            {
                "id": cart_item.id,
                "item_id": cart_item.item.id,
                "customer_id": cart_item.customer.id,
                "quantity": cart_item.quantity,
            }
        )

    @staticmethod
    def delete(request, id):
        try:
            cart_item = CartItem.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        cart_item.delete()
        return ok_status()
