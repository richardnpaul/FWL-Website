# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Page.menu'
        db.alter_column(u'pages_page', 'menu_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Menu'], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Page.menu'
        raise RuntimeError("Cannot reverse this migration. 'Page.menu' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Page.menu'
        db.alter_column(u'pages_page', 'menu_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Menu']))

    models = {
        u'pages.menu': {
            'Meta': {'object_name': 'Menu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'pages.page': {
            'Meta': {'object_name': 'Page'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.Menu']", 'null': 'True', 'blank': 'True'}),
            'parent_page': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'blank': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['pages']