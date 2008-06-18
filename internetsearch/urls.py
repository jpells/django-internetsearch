from django.conf.urls.defaults import *
from internetsearch import views

urlpatterns = patterns('',
    url(r'^$', views.search, name="internetsearch_search"),
    url(r'^(?P<term>[-\w]+)/$', views.search, name="internetsearch_search_term"),
    url(r'^(?P<term>[-\w]+)/(?P<results_number>\d+)/$', views.search, name="internetsearch_search_term_results"),
)
