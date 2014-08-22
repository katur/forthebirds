# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Species.absolute_ordering'
        db.delete_column(u'birds_species', 'absolute_ordering')

        # Adding field 'Species.absolute_position'
        db.add_column(u'birds_species', 'absolute_position',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True),
                      keep_default=False)

        # Deleting field 'TaxonomicGroup.sibling_ordering'
        db.delete_column(u'birds_taxonomicgroup', 'sibling_ordering')

        # Adding field 'TaxonomicGroup.position_within_siblings'
        db.add_column(u'birds_taxonomicgroup', 'position_within_siblings',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Species.absolute_ordering'
        db.add_column(u'birds_species', 'absolute_ordering',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True),
                      keep_default=False)

        # Deleting field 'Species.absolute_position'
        db.delete_column(u'birds_species', 'absolute_position')

        # Adding field 'TaxonomicGroup.sibling_ordering'
        db.add_column(u'birds_taxonomicgroup', 'sibling_ordering',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True),
                      keep_default=False)

        # Deleting field 'TaxonomicGroup.position_within_siblings'
        db.delete_column(u'birds_taxonomicgroup', 'position_within_siblings')


    models = {
        u'birds.species': {
            'Meta': {'object_name': 'Species'},
            'absolute_position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
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
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['birds.TaxonomicGroup']"})
        },
        u'birds.taxonomicgroup': {
            'Meta': {'object_name': 'TaxonomicGroup'},
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['birds.TaxonomicLevel']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['birds.TaxonomicGroup']", 'null': 'True', 'blank': 'True'}),
            'position_within_siblings': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'})
        },
        u'birds.taxonomiclevel': {
            'Meta': {'object_name': 'TaxonomicLevel'},
            'depth': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['birds']