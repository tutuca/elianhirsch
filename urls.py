from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'catalog.views.index', {}, 'index'),
    (r'^gallery/(?P<serie_slug>[^/]+)$', 'catalog.views.gallery', {}, 'gallery'),
#     (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
