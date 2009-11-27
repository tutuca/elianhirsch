from django.views.generic import list_detail
from models import Serie, Foto

def index(request):
    series = Serie.objects.all()
    last_serie = Serie.objects.latest('created')
    return list_detail.object_detail(request, 
                series,
                slug=last_serie.slug,
                template_name='index.html')
                
def work(request):
    series = Serie.objects.all()
    return list_detail.object_list(request, 
                series,
                paginate_by=4,
                template_name='work.html')

def serie(request, serie_slug):
    series = Serie.objects.all()
    return list_detail.object_detail(request, 
                series,
                slug=serie_slug,
                template_name='serie.html')


def gallery(request, serie_slug):
    serie = Serie.objects.get(slug=serie_slug)
    fotos = serie.foto_set.all()
    return list_detail.object_list(request, 
                fotos,
                paginate_by=5,
                extra_context={'serie':serie},
                template_name='gallery.html')

def foto(request, foto_id):
    fotos = Foto.objects.all()
    return list_detail.object_detail(request, 
                fotos,
                object_id=foto_id,
                extra_context={'object_list':fotos},
                template_name='foto.html')
