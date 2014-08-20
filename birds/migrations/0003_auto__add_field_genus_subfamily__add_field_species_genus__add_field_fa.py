# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Genus.subfamily'
        db.add_column(u'birds_genus', 'subfamily',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['birds.Subfamily']),
                      keep_default=False)

        # Adding field 'Species.genus'
        db.add_column(u'birds_species', 'genus',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['birds.Genus']),
                      keep_default=False)

        # Adding field 'Family.order'
        db.add_column(u'birds_family', 'order',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['birds.Order']),
                      keep_default=False)

        # Adding field 'Subfamily.family'
        db.add_column(u'birds_subfamily', 'family',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['birds.Family']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Genus.subfamily'
        db.delete_column(u'birds_genus', 'subfamily_id')

        # Deleting field 'Species.genus'
        db.delete_column(u'birds_species', 'genus_id')

        # Deleting field 'Family.order'
        db.delete_column(u'birds_family', 'order_id')

        # Deleting field 'Subfamily.family'
        db.delete_column(u'birds_subfamily', 'family_id')


    models = {
        u'birds.family': {
            'Meta': {'object_name': 'Family'},
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['birds.Order']"})
        },
        u'birds.genus': {
            'Meta': {'object_name': 'Genus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'subfamily': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['birds.Subfamily']"})
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
            'genus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['birds.Genus']"}),
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
            'family': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['birds.Family']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['birds']