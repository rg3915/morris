from django.conf.urls import patterns, include, url
from django.contrib import admin
from myproject.core.views import *

urlpatterns = patterns(
    'myproject.core.views',
    url(r'^$', 'index', name='index'),
    url(r'^morris/$', 'morris', name='morris'),
    url(r'^morris_data/$', 'morris_dataview', name='morris_data'),
    url(r'^persons-by-uf/$', PersonsUFView.as_view(), name='persons_by_uf'),
    url(r'^uf/$', 'uf_json', name='uf_json'),
    url(r'^download/$', 'download', name='download'),
    url(r'^about/$', 'about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
)
