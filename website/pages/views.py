from django.shortcuts import render_to_response
from django.template import RequestContext
from pages.models import Page, Menu

# Create your views here.

def page(request, pageslug):
    template = Page.objects.get(slug=pageslug)
    context = {'pages': Page.objects.get(slug=pageslug), 
               'navigation': Page.objects.all()}
    return render_to_response(template.template, context, 
                              context_instance=RequestContext(request))