from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.sitemaps import Sitemap
from pages.models import Page, Menu


# Create your views here.
def home(request):
    context = {'pages': Page.objects.get(slug='home'), 
               'navigation': Page.objects.all()}
    return render_to_response('home.html', context, 
                              context_instance=RequestContext(request))
