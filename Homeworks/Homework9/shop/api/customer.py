import json

from django.views.generic import View
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from ..models.Customer import Customer

from ..utils import data_status, ok_status


class CustomerView(View):
    
    def get(self, request):
        customers = Customer.objects.all()
        data = []
        for customer in customers:
            data.append({
                "id": customer.id,
                "user_id": customer.user.id,
                "avatar": str(customer.avatar),
                "registrated_at": customer.registrated_at.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            })
        return data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        customer = Customer.objects.create(
            user_id=data['user_id'],
            avatar=data['avatar'],
            registered_at=data['registered_at'],
        )
        customer.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return CustomerView.get_single(request, id)
        if request.method == "DELETE":
            return CustomerView.delete(request, id)
        if request.method == "PATCH":
            return CustomerView.edit(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            customer = Customer.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return data_status({
            "id": customer.id,
            "user_id": customer.user.id,
            "avatar": str(customer.avatar),
            "registrated_at": customer.registrated_at.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
        })

    @staticmethod
    def delete(request, id):
        try:
            customer = Customer.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        customer.delete()
        return ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            customer = Customer.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "user_id" in data:
            customer.user_id = data['user_id']
        if "avatar" in data:
            customer.avatar = data['avatar']
        if "registered_at" in data:
            customer.registered_at = data['registered_at']
        customer.save()
        return ok_status()
