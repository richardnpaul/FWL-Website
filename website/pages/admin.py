from django.contrib import admin
from pages.models import Page, Menu

class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'template', 'parent_page', 'slug')
    prepopulated_fields = {'slug': ('title',)}

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    prepopulated_fields = {'slug': ('title',)}    

admin.site.register(Page, PageAdmin)
admin.site.register(Menu, MenuAdmin)