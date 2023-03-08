import json

from django.views.generic import View
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from ..models.StoreOwner import StoreOwner

from ..utils import data_status, ok_status


class StoreOwnerView(View):
   
    def get(self, request):
        owners = StoreOwner.objects.all()
        data = []
        for owner in owners:
            data.append({"id": owner.id, "user_id": owner.user.id, "avatar": owner.avatar, "registered_at": owner.registered_at})
        return data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        owner = StoreOwner.objects.create(
            user_id=data['user_id'],
            avatar=data.get('avatar', None),
            registered_at=data.get('registered_at', None)
        )
        owner.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreOwnerView.get_single(request, id)
        if request.method == "DELETE":
            return StoreOwnerView.delete(request, id)
        if request.method == "PATCH":
            return StoreOwnerView.edit(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            owner = StoreOwner.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return data_status({"id": owner.id, "user_id": owner.user.id, "avatar": owner.avatar, "registered_at": owner.registered_at})

    @staticmethod
    def delete(request, id):
        try:
            owner = StoreOwner.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        owner.delete()
        return ok_status()