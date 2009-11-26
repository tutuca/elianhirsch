from django.db import models
from django.template.defaultfilters import slugify

from PIL import Image
import mptt


class Foto(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='images', blank= True)
   
    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        filehead, filetail = os.path.split(self.image.path)
        return filetail

#    def save(self, *args, **kwargs):

#        galeria_name = slugify(self.galeria.title)
#        upload_to = self.image.field.upload_to
#        if galeria_name not in upload_to.split('/'):
#            upload_to = 'images/%s'%(galeria_name,)        

#        self.image.field.upload_to = upload_to

#        super(Foto, self).save(*args, **kwargs)


class Category (models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=60)
    parent = models.ForeignKey('Category')
    
class Serie (models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=60)
    description = model.TextField()
    pictures = models.ForeignKey('Foto')
    


try:
    mptt.register(Categoria, order_insertion_by=['nombre'])
except mptt.AlreadyRegistered():
    
    
