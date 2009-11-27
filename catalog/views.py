from django.views.generic import list_detail
from models import Serie

def index(request):
    series = Serie.objects.all()
    last_serie = Serie.objects.latest('created')
    
    return list_detail.object_detail(request, 
                series,
                slug=last_serie.slug,
                template_name='index.html')

def gallery(request, serie_slug):
    series = Serie.objects.all()
    return list_detail.object_detail(request, 
                series,
                slug=serie_slug,
                template_name='gallery.html')

