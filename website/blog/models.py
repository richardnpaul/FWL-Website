from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField()
    pub_date = models.DateTimeField('Date Published', auto_now_add=True)
    published = models.BooleanField()
    blog_slug = models.SlugField(unique=True)
    
    def __unicode__(self):
        return self.title