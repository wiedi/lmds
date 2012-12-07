from django.http import HttpResponse, HttpResponseNotFound
from models import *


def get_instance(request):
    return Instance.objects.get(ipv4 = request.META['REMOTE_ADDR'])

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
    calls = """amiid
ami-launch-index
ami-manifest-path
block-device-mapping/
hostname
instance-action
instance-id
instance-type
kernel-id
local-hostname
local-ipv4
ipv4-associations
mac
network/
placement/
public-hostname
public-ipv4
public-keys/
reservation-id
security-groups
"""
    return HttpResponse(calls, content_type = "text/plain")


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