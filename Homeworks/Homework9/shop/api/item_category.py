import json

from django.views.generic import View
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from ..models.ItemCategory import ItemCategory

from ..utils import data_status, ok_status

class ItemCategoryView(View):
    
    def get(self, request):
        categories = ItemCategory.objects.all()
        data = []
        for category in categories:
            data.append({"name": category.name, "id": category.id})
        return data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        category = ItemCategory.objects.create(
            name=data['name']
        )
        category.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return ItemCategoryView.get_single(request, id)
        if request.method == "DELETE":
            return ItemCategoryView.delete(request, id)
        if request.method == "PATCH":
            return ItemCategoryView.edit(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            category = ItemCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return data_status({"id": category.id, "name": category.name})

    @staticmethod
    def delete(request, id):
        try:
            category = ItemCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        
        category.delete()
        return ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            category = ItemCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            category.name = data['name']
        category.save()
        return ok_status()
