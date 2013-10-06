from django.contrib import admin
from blog.models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'pub_date', 'published')
    prepopulated_fields = {'blog_slug': ('title',)}
    #exclude = ('blog_slug',)    causes exception of blog_slug not found in form
    

admin.site.register(Blog, BlogAdmin)