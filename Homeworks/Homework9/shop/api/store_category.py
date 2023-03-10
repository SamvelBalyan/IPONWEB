import json

from django.views.generic import View
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from ..models.StoreCategory import StoreCategory

from ..utils import data_status, ok_status


class StoreCategoryView(View):
    
    def get(self, request):
        categories = StoreCategory.objects.all()
        data = []
        for category in categories:
            data.append({"name": category.name, "id": category.id})
        return data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        category = StoreCategory.objects.create(
            name=data['name']
        )
        category.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreCategoryView.get_single(request, id)
        if request.method == "DELETE":
            return StoreCategoryView.delete(request, id)
        if request.method == "PATCH":
            return StoreCategoryView.edit(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            category = StoreCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return data_status({"id": category.id, "name": category.name})

    @staticmethod
    def delete(request, id):
        try:
            category = StoreCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        category.delete()
        return ok_status()