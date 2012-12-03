from django.conf.urls import url, patterns

urlpatterns = patterns('laws.views',
    url(r'^$',              'api_version'),
    url(r'^(?P<version>[^/]+)/meta-data/instance-id$', 'instance_id'),
    url(r'^(?P<version>[^/]+)/meta-data/user-data$',   'user_data'),
)
