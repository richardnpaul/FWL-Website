from django.shortcuts import render_to_response
from blog.models import Blog
from pages.models import Page
# Create your views here.

def blog_all(request):
    return render_to_response('blog.html',
                              {'blogs': Blog.objects.all(),
                               'pages': Page.objects.get(slug='blog') })

def blog_instance(request, blog_slug):
    return render_to_response('blog_instance.html',
                              {'blog': Blog.objects.get(blog_slug=blog_slug), 
                               'pages': Page.objects.get(slug='blog') })    