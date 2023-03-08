import json

from django.http import HttpResponse

@staticmethod
def data_status(data):
    return HttpResponse(
        json.dumps({"data": data, "status": "ok"}),
        status=200,
        content_type="application/json",
    )

@staticmethod
def ok_status():
    return HttpResponse(
        json.dumps({"status": "ok"}), status=200, content_type="application/json"
    )