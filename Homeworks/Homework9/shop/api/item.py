import json

from django.views.generic import View
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from ..models.Item import Item
from ..models.ItemCategory import ItemCategory

from ..utils import data_status, ok_status


class ItemView(View):
    
    def get(self, request):
        items = Item.objects.all()
        data = []
        for item in items:
            data.append({
                "id": item.id,
                "name": item.name,
                "picture": item.picture.url,
                "category": {
                    "id": item.category.id,
                    "name": item.category.name,
                    "picture": item.category.picture.url
                },
                "price": item.price,
                "quantity": item.quantity,
                "info": item.info,
                "store": {
                    "id": item.store.id,
                    "name": item.store.name
                }
            })
        return data_status(data)

    def post(self, request):
        data = json.loads(request.body)

        # Create the item category if it doesn't exist
        category, created = ItemCategory.objects.get_or_create(
            id=data['category_id']
        )

        # Create the item
        item = Item.objects.create(
            name=data['name'],
            picture=data['picture'],
            category=category,
            price=data['price'],
            quantity=data['quantity'],
            info=data['info'],
            store_id=data['store_id']
        )
        item.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return ItemView.get_single(request, id)
        if request.method == "DELETE":
            return ItemView.delete(request, id)
        if request.method == "PATCH":
            return ItemView.edit(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            item = Item.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        data = {
            "id": item.id,
            "name": item.name,
            "picture": item.picture.url,
            "category": {
                "id": item.category.id,
                "name": item.category.name,
                "picture": item.category.picture.url
            },
            "price": item.price,
            "quantity": item.quantity,
            "info": item.info,
            "store": {
                "id": item.store.id,
                "name": item.store.name
            }
        }
        return data_status(data)

    @staticmethod
    def delete(request, id):
        try:
            item = Item.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        item.delete()
        return ok_status()
