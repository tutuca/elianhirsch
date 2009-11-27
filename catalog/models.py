from django.db import models
from django.template.defaultfilters import slugify
from PIL import Image
import mptt
import os

class Foto(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='images', blank= True)
    created = models.DateTimeField(auto_now_add=True, editable = False)
    serie = models.ForeignKey('Serie')
    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        filehead, filetail = os.path.split(self.image.path)
        return filetail

    def save(self, *args, **kwargs):


        upload_to = self.image.field.upload_to
        if self.serie.slug not in upload_to.split('/'):
            upload_to = 'images/%s'%(self.serie.slug,)        

        self.image.field.upload_to = upload_to

        super(Foto, self).save(*args, **kwargs)


class Category (models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=60)
    parent = models.ForeignKey('Category', blank= True, null=True)
    
    def __unicode__(self):
        return self.name

    class Meta ():
        verbose_name_plural = 'Categories'
    
class Serie (models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=60)
    description = models.TextField()
    category = models.ForeignKey('Category')

    def __unicode__(self):
        return self.name

    
try: 
    mptt.register(Category)  
except mptt.AlreadyRegistered:
    '''Fail Silently'''
    pass
    
    
