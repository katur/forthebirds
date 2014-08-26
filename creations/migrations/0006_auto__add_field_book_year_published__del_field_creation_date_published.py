# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Book.year_published'
        db.add_column(u'creations_book', 'year_published',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Creation.date_published'
        db.delete_column(u'creations_creation', 'date_published')

        # Adding field 'RadioProgram.original_air_date'
        db.add_column(u'creations_radioprogram', 'original_air_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Book.year_published'
        db.delete_column(u'creations_book', 'year_published')

        # Adding field 'Creation.date_published'
        db.add_column(u'creations_creation', 'date_published',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'RadioProgram.original_air_date'
        db.delete_column(u'creations_radioprogram', 'original_air_date')


    models = {
        u'creations.book': {
            'Meta': {'ordering': "['-year_published']", 'object_name': 'Book', '_ormbases': [u'creations.Creation']},
            u'creation_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['creations.Creation']", 'unique': 'True', 'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'purchase_url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'year_published': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'creations.creation': {
            'Meta': {'object_name': 'Creation'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'creations.radioprogram': {
            'Meta': {'ordering': "['-original_air_date']", 'object_name': 'RadioProgram', '_ormbases': [u'creations.Creation']},
            u'creation_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['creations.Creation']", 'unique': 'True', 'primary_key': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'original_air_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'transcript': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['creations']