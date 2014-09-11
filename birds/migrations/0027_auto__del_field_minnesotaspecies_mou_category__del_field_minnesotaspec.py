# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'MinnesotaSpecies.mou_category'
        db.delete_column(u'birds_minnesotaspecies', 'mou_category')

        # Deleting field 'MinnesotaSpecies.mou_notes'
        db.delete_column(u'birds_minnesotaspecies', 'mou_notes')

        # Adding field 'MinnesotaSpecies.mou_status'
        db.add_column(u'birds_minnesotaspecies', 'mou_status',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'MinnesotaSpecies.mou_breeding_status'
        db.add_column(u'birds_minnesotaspecies', 'mou_breeding_status',
                      self.gf('django.db.models.fields.NullBooleanField')(default=None, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MinnesotaSpecies.mou_annotation'
        db.add_column(u'birds_minnesotaspecies', 'mou_annotation',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'MinnesotaSpecies.mou_category'
        db.add_column(u'birds_minnesotaspecies', 'mou_category',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'MinnesotaSpecies.mou_notes'
        db.add_column(u'birds_minnesotaspecies', 'mou_notes',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Deleting field 'MinnesotaSpecies.mou_status'
        db.delete_column(u'birds_minnesotaspecies', 'mou_status')

        # Deleting field 'MinnesotaSpecies.mou_breeding_status'
        db.delete_column(u'birds_minnesotaspecies', 'mou_breeding_status')

        # Deleting field 'MinnesotaSpecies.mou_annotation'
        db.delete_column(u'birds_minnesotaspecies', 'mou_annotation')


    models = {
        u'birds.minnesotaspecies': {
            'Meta': {'ordering': "['species__absolute_position']", 'object_name': 'MinnesotaSpecies'},
            'include_in_book': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'mou_annotation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'mou_breeding_status': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'mou_status': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'range_in_minnesota': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'species': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['birds.Species']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'birds.species': {
            'Meta': {'ordering': "['absolute_position']", 'object_name': 'Species'},
            'absolute_position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'bird_of_the_week_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'blurb': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'french_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'is_hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'main_photo_url': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'nacc_annotation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'nacc_is_accidental': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'nacc_is_extinct': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'nacc_is_hawaiian': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'nacc_is_introduced': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'nacc_is_misplaced': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'nacc_is_nonbreeding': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['birds.TaxonomicGroup']"})
        },
        u'birds.taxonomicgroup': {
            'Meta': {'ordering': "['level__depth', 'relative_position']", 'object_name': 'TaxonomicGroup'},
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['birds.TaxonomicLevel']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['birds.TaxonomicGroup']", 'null': 'True', 'blank': 'True'}),
            'relative_position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'})
        },
        u'birds.taxonomiclevel': {
            'Meta': {'object_name': 'TaxonomicLevel'},
            'depth': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['birds']