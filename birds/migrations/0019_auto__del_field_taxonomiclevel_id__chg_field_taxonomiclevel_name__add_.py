# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'TaxonomicLevel.id'
        db.delete_column(u'birds_taxonomiclevel', u'id')


        # Changing field 'TaxonomicLevel.name'
        db.alter_column(u'birds_taxonomiclevel', 'name', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True))
        # Adding unique constraint on 'TaxonomicLevel', fields ['name']
        db.create_unique(u'birds_taxonomiclevel', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'TaxonomicLevel', fields ['name']
        db.delete_unique(u'birds_taxonomiclevel', ['name'])

        # Adding field 'TaxonomicLevel.id'
        db.add_column(u'birds_taxonomiclevel', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=1, primary_key=True),
                      keep_default=False)


        # Changing field 'TaxonomicLevel.name'
        db.alter_column(u'birds_taxonomiclevel', 'name', self.gf('django.db.models.fields.CharField')(max_length=20))

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
            'level': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['birds.TaxonomicLevel']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['birds.TaxonomicGroup']", 'null': 'True', 'blank': 'True'}),
            'position_within_siblings': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'})
        },
        u'birds.taxonomiclevel': {
            'Meta': {'object_name': 'TaxonomicLevel'},
            'depth': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'})
        }
    }

    complete_apps = ['birds']