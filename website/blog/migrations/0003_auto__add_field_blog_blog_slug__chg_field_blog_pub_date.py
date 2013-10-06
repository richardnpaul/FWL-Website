# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Blog.blog_slug'
        db.add_column(u'blog_blog', 'blog_slug',
                      self.gf('django.db.models.fields.SlugField')(default='slug', unique=True, max_length=50),
                      keep_default=False)


        # Changing field 'Blog.pub_date'
        db.alter_column(u'blog_blog', 'pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    def backwards(self, orm):
        # Deleting field 'Blog.blog_slug'
        db.delete_column(u'blog_blog', 'blog_slug')


        # Changing field 'Blog.pub_date'
        db.alter_column(u'blog_blog', 'pub_date', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        u'blog.blog': {
            'Meta': {'object_name': 'Blog'},
            'blog_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'body': ('ckeditor.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['blog']