# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WayToHelp'
        db.create_table(u'waystohelp_waytohelp', (
            ('id', self.gf('django.db.models.fields.PositiveIntegerField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'waystohelp', ['WayToHelp'])


    def backwards(self, orm):
        # Deleting model 'WayToHelp'
        db.delete_table(u'waystohelp_waytohelp')


    models = {
        u'waystohelp.waytohelp': {
            'Meta': {'ordering': "['id']", 'object_name': 'WayToHelp'},
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['waystohelp']