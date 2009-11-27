from django.conf import settings
from django.conf.urls.defaults import url, patterns, include
from django.contrib import admin
from django.views.generic.simple import direct_to_template
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'catalog.views.index', {}, 'index'),
    (r'^work/$', 'catalog.views.work', {}, 'work'),
    (r'^foto/(?P<foto_id>\d+)$', 'catalog.views.foto', {}, 'foto'),
    (r'^work/serie/(?P<serie_slug>[^/]+)$', 'catalog.views.serie', {}, 'serie'),
    (r'^work/gallery/(?P<serie_slug>[^/]+)$', 'catalog.views.gallery', {}, 'gallery'),
    (r'^about/$', direct_to_template,{'template':'about.html'},'about'),    
    (r'^contact/$', direct_to_template,{'template':'contact.html'},'contact'),    
#     (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
     {'document_root': settings.MEDIA_ROOT}),
)
