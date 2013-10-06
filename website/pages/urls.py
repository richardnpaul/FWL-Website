from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^website/', include('website.foo.urls')),                       
    url(r'^(?P<pageslug>.*)/$', 'pages.views.page'),
)