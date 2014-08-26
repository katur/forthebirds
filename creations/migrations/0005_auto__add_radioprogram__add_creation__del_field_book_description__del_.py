# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RadioProgram'
        db.create_table(u'creations_radioprogram', (
            (u'creation_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['creations.Creation'], unique=True, primary_key=True)),
            ('transcript', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'creations', ['RadioProgram'])

        # Adding model 'Creation'
        db.create_table(u'creations_creation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('date_published', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'creations', ['Creation'])

        # Deleting field 'Book.description'
        db.delete_column(u'creations_book', 'description')

        # Deleting field 'Book.title'
        db.delete_column(u'creations_book', 'title')

        # Deleting field 'Book.id'
        db.delete_column(u'creations_book', u'id')

        # Deleting field 'Book.year_published'
        db.delete_column(u'creations_book', 'year_published')

        # Adding field 'Book.creation_ptr'
        db.add_column(u'creations_book', u'creation_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['creations.Creation'], unique=True, primary_key=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'RadioProgram'
        db.delete_table(u'creations_radioprogram')

        # Deleting model 'Creation'
        db.delete_table(u'creations_creation')

        # Adding field 'Book.description'
        db.add_column(u'creations_book', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Book.title'
        db.add_column(u'creations_book', 'title',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)

        # Adding field 'Book.id'
        db.add_column(u'creations_book', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=1, primary_key=True),
                      keep_default=False)

        # Adding field 'Book.year_published'
        db.add_column(u'creations_book', 'year_published',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Book.creation_ptr'
        db.delete_column(u'creations_book', u'creation_ptr_id')


    models = {
        u'creations.book': {
            'Meta': {'ordering': "['-date_published']", 'object_name': 'Book', '_ormbases': [u'creations.Creation']},
            u'creation_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['creations.Creation']", 'unique': 'True', 'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'purchase_url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        },
        u'creations.creation': {
            'Meta': {'ordering': "['-date_published']", 'object_name': 'Creation'},
            'date_published': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'creations.radioprogram': {
            'Meta': {'ordering': "['-date_published']", 'object_name': 'RadioProgram', '_ormbases': [u'creations.Creation']},
            u'creation_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['creations.Creation']", 'unique': 'True', 'primary_key': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'transcript': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['creations']