from django.http import HttpResponse, HttpResponseNotFound
from models import *


def get_instance(request):
    try:
        return Instance.objects.get(ipv4 = request.META['REMOTE_ADDR'])
    except:
        return None

def api_version(request):
    versions = [
        '1.0',
        '2007-01-19',
        '2007-03-01',
        '2007-08-29',
        '2007-10-10',
        '2007-12-15',
        '2008-02-01',
        '2008-09-01',
        '2009-04-04',
        '2011-01-01',
    ]
    return HttpResponse("\n".join(versions), content_type = "text/plain")

def meta_data(request, version):
    calls = [
        "instance-id",
        "hostname",
        "local-hostname"
    ]
    return HttpResponse("\n".join(calls), content_type = "text/plain")


def instance_id(request, version):
    i = get_instance(request)
    if not i: return HttpResponseNotFound("", content_type = "text/plain")
    
    return HttpResponse(i.instance_id(), content_type = "text/plain")


def user_data(request, version):
    i = get_instance(request)
    if not i: return HttpResponseNotFound("", content_type = "text/plain")
    
    return HttpResponse(i.user_data, content_type = "text/plain")

def hostname(request, version):
    i = get_instance(request)
    if not i: return HttpResponseNotFound("", content_type = "text/plain")
    
    return HttpResponse(i.hostname, content_type = "text/plain")


def local_hostname(request, version):
    i = get_instance(request)
    if not i: return HttpResponseNotFound("", content_type = "text/plain")
    
    return HttpResponse(i.hostname.split('.')[0], content_type = "text/plain")