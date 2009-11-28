from django.conf import settings
from django.conf.urls.defaults import url, patterns, include
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from catalog.models import Serie

admin.autodiscover()

context=dict(last_serie = Serie.objects.latest('created'))

urlpatterns = patterns('',
    (r'^$', 'catalog.views.index', {}, 'index'),
    (r'^work/$', 'catalog.views.work', {}, 'work'),
    (r'^work/gallery/(?P<serie_slug>[^/]+)$', 'catalog.views.gallery', {}, 'gallery'),
    (r'^work/(?P<cat_slug>[^/]+)$', 'catalog.views.work', {}, 'work'),
    (r'^work/(?P<cat_slug>[^/]+)/(?P<serie_slug>[^/]+)$', 'catalog.views.serie', {}, 'serie'),
    (r'^foto/(?P<foto_id>\d+)$', 'catalog.views.foto', {}, 'foto'),
    (r'^about/$', direct_to_template,{'template':'about.html','extra_context':context},'about'),    
    (r'^contact/$', direct_to_template,{'template':'contact.html','extra_context':context},'contact'),    
#     (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
     {'document_root': settings.MEDIA_ROOT}),
)
