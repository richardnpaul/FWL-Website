from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^website/', include('website.foo.urls')), 
    url(r'^$', 'blog.views.blog_all'),
    url(r'^(?P<blog_slug>.*)/$', 'blog.views.blog_instance') 
)