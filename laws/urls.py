from django.conf.urls import url, patterns

urlpatterns = patterns('laws.views',
    url(r'^$',              'api_version'),
    url(r'^(?P<version>[^/]+)/meta-data/$',               'meta_data'),
    url(r'^(?P<version>[^/]+)/meta-data/instance-id$',    'instance_id'),
    url(r'^(?P<version>[^/]+)/meta-data/hostname',        'hostname'),
    url(r'^(?P<version>[^/]+)/meta-data/local-hostname$', 'local_hostname'),
    url(r'^(?P<version>[^/]+)/meta-data/mac$',            'mac'),
    url(r'^(?P<version>[^/]+)/user-data$',                'user_data'),
)
