import json

from django.views.generic import View
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from ..models.Store import Store
from ..models.StoreOwner import StoreOwner
from ..models.StoreCategory import StoreCategory
from ..models.Item import Item

from ..utils import data_status, ok_status

class StoreView(View):

    def get(self, request):
        stores = Store.objects.all()
        data = []
        for store in stores:
            data.append({
                "name": store.name, 
                "id": store.id,
                "owner": store.owner.id,
                "store_category": store.store_category.id
            })
        return data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        owner = StoreOwner.objects.get(id=data['owner'])
        store_category = StoreCategory.objects.get(id=data['store_category'])
        store = Store.objects.create(
            name=data['name'],
            owner=owner,
            store_category=store_category
        )
        store.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreView.get_single(request, id)
        if request.method == "DELETE":
            return StoreView.delete(request, id)
        if request.method == "PATCH":
            return StoreView.edit(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            store = Store.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        items = list(Item.objects.filter(store=store).values())
        # items = list(items.values())

        return data_status({
            "id": store.id, 
            "name": store.name, 
            "owner": store.owner.id, 
            "store_category": store.store_category.id,
            "items":items,
        })

    @staticmethod
    def delete(request, id):
        try:
            store = Store.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        
        store.delete()
        return ok_status()
