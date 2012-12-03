from django.http import HttpResponse, HttpResponseNotFound
from models import *


def get_instance(request):
    return Instance.objects.get(ip = request.META['REMOTE_ADDR'])


def instance_id(request, version):
    i = get_instance(request)
    
    if not i:
        return HttpResponseNotFound("", content_type = "text/plain")
    
    return HttpResponse(i.instance_id(), content_type = "text/plain")


def user_data(request, version):
    i = get_instance(request)
    
    if not i:
        return HttpResponseNotFound("", content_type = "text/plain")
    
    return HttpResponse(i.user_data, content_type = "text/plain")