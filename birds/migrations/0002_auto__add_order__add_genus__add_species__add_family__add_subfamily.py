# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Order'
        db.create_table(u'birds_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
        ))
        db.send_create_signal(u'birds', ['Order'])

        # Adding model 'Genus'
        db.create_table(u'birds_genus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
        ))
        db.send_create_signal(u'birds', ['Genus'])

        # Adding model 'Species'
        db.create_table(u'birds_species', (
            ('id', self.gf('django.db.models.fields.PositiveIntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('common_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('french_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nacc_annotation', self.gf('django.db.models.fields.TextField')()),
            ('nacc_is_accidental', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('nacc_is_hawaiian', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('nacc_is_introduced', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('nacc_is_nonbreeding', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('nacc_is_extinct', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('nacc_is_misplaced', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'birds', ['Species'])

        # Adding model 'Family'
        db.create_table(u'birds_family', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('common_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'birds', ['Family'])

        # Adding model 'Subfamily'
        db.create_table(u'birds_subfamily', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
        ))
        db.send_create_signal(u'birds', ['Subfamily'])


    def backwards(self, orm):
        # Deleting model 'Order'
        db.delete_table(u'birds_order')

        # Deleting model 'Genus'
        db.delete_table(u'birds_genus')

        # Deleting model 'Species'
        db.delete_table(u'birds_species')

        # Deleting model 'Family'
        db.delete_table(u'birds_family')

        # Deleting model 'Subfamily'
        db.delete_table(u'birds_subfamily')


    models = {
        u'birds.family': {
            'Meta': {'object_name': 'Family'},
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'birds.genus': {
            'Meta': {'object_name': 'Genus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'birds.order': {
            'Meta': {'object_name': 'Order'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'birds.species': {
            'Meta': {'object_name': 'Species'},
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'french_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'nacc_annotation': ('django.db.models.fields.TextField', [], {}),
            'nacc_is_accidental': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'nacc_is_extinct': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'nacc_is_hawaiian': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'nacc_is_introduced': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'nacc_is_misplaced': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'nacc_is_nonbreeding': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'birds.subfamily': {
            'Meta': {'object_name': 'Subfamily'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['birds']