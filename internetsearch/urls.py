from django.conf.urls.defaults import *

urlpatterns = patterns('internetsearch.views',
    (r'^$', 'search'),
    (r'^(?P<term>[-\w]+)/$', 'search'),
    (r'^(?P<term>[-\w]+)/(?P<results_number>\d+)/$', 'search'),
)
