from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=160)
    keywords = models.TextField()
    template = models.CharField(max_length=30, unique=True)
    parent_page = models.CharField(max_length=30, blank=True)
    slug = models.SlugField(unique=True)
    menu = models.ForeignKey('Menu', null=True, blank=True)
    published = models.BooleanField()
    analytics = models.CharField(max_length=30, unique=True, null=True, blank=True)
    
    # include this to give the model object a name in the admin interface
    def __unicode__(self):
        return self.title

class Menu(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, editable=False)
    
    def __unicode__(self):
        return self.title