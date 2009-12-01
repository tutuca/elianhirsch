from django.views.generic import list_detail
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.conf import settings
from django.template.context import RequestContext
from django.core.mail import EmailMessage
from models import Serie, Foto, Category
from logging import log, info, error

def index(request):
    series = Serie.objects.all()
    last_serie = Serie.objects.latest('created')
    return list_detail.object_detail(request, 
                series,
                slug=last_serie.slug,
                template_name='index.html')
                
def work(request, cat_slug=None):
    category = None
    if cat_slug :
        category = get_object_or_404(Category,slug=cat_slug)
        series = Serie.objects.filter(category=category.id)
    else :
        series = Serie.objects.all()
    
    return list_detail.object_list(request, 
                series,
                paginate_by=4,
                extra_context={'category':category},
                template_name='work.html')

def serie(request,cat_slug, serie_slug):
    if cat_slug :
        category = get_object_or_404(Category,slug=cat_slug)
        series = Serie.objects.filter(category=category.id)
    else :
        series = Serie.objects.all()

    return list_detail.object_detail(request, 
                series,
                slug=serie_slug,
                extra_context={'category':category},
                template_name='serie.html')


def gallery(request, serie_slug):
    serie = get_object_or_404(Serie,slug=serie_slug)
    fotos = serie.foto_set.all()
    return list_detail.object_list(request, 
                fotos,
                paginate_by=12,
                extra_context={'serie':serie,'category':serie.category},
                template_name='gallery.html')

def foto(request, foto_id):
    fotos = Foto.objects.all()
    category = fotos.get(id=foto_id).serie.category

    return list_detail.object_detail(request, 
                fotos,
                object_id=foto_id,
                extra_context={'object_list':fotos,'category':category},
                template_name='foto.html')
                
def mail(request,*args,**kwargs):
    import pdb
    if request.method == 'POST':
        if not request.POST['name'] or not request.POST['email']:
            ''' Redirect to the form with an error message showing 
            the required fields '''
            pass
        if request.POST['honeypot']:
            error(request)
            return redirect('/')                
            
        else :
            subject = 'Nuevo mensaje de %s desde la web' %request.POST['name']
            email = EmailMessage(subject=subject, 
                        body=request.POST['message'],
                        from_email=request.POST['email'],
                        to=('elianhirsch@gmail.com',),
                        bcc=('maturburu@gmail.com',))
            if not settings.DEBUG :                
                email.send()
            else :
                info(email)
                
    return render_to_response('mail_sent.html', 
                {'last_serie':Serie.objects.latest('created')}
                )
    
