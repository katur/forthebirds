# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Species.genus'
        db.delete_column(u'birds_species', 'genus')


        # Renaming column for 'Species.family' to match new field type.
        db.rename_column(u'birds_species', 'family', 'family_id')
        # Changing field 'Species.family'
        db.alter_column(u'birds_species', 'family_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['birds.TaxonomicGroup']))
        # Adding index on 'Species', fields ['family']
        db.create_index(u'birds_species', ['family_id'])


        # Renaming column for 'Species.subfamily' to match new field type.
        db.rename_column(u'birds_species', 'subfamily', 'subfamily_id')
        # Changing field 'Species.subfamily'
        db.alter_column(u'birds_species', 'subfamily_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['birds.TaxonomicGroup']))
        # Adding index on 'Species', fields ['subfamily']
        db.create_index(u'birds_species', ['subfamily_id'])


        # Renaming column for 'Species.order' to match new field type.
        db.rename_column(u'birds_species', 'order', 'order_id')
        # Changing field 'Species.order'
        db.alter_column(u'birds_species', 'order_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['birds.TaxonomicGroup']))
        # Adding index on 'Species', fields ['order']
        db.create_index(u'birds_species', ['order_id'])


    def backwards(self, orm):
        # Removing index on 'Species', fields ['order']
        db.delete_index(u'birds_species', ['order_id'])

        # Removing index on 'Species', fields ['subfamily']
        db.delete_index(u'birds_species', ['subfamily_id'])

        # Removing index on 'Species', fields ['family']
        db.delete_index(u'birds_species', ['family_id'])

        # Adding field 'Species.genus'
        db.add_column(u'birds_species', 'genus',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=30),
                      keep_default=False)


        # Renaming column for 'Species.family' to match new field type.
        db.rename_column(u'birds_species', 'family_id', 'family')
        # Changing field 'Species.family'
        db.alter_column(u'birds_species', 'family', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Renaming column for 'Species.subfamily' to match new field type.
        db.rename_column(u'birds_species', 'subfamily_id', 'subfamily')
        # Changing field 'Species.subfamily'
        db.alter_column(u'birds_species', 'subfamily', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Renaming column for 'Species.order' to match new field type.
        db.rename_column(u'birds_species', 'order_id', 'order')
        # Changing field 'Species.order'
        db.alter_column(u'birds_species', 'order', self.gf('django.db.models.fields.CharField')(max_length=30))

    models = {
        u'birds.species': {
            'Meta': {'ordering': "['absolute_position']", 'object_name': 'Species'},
            'absolute_position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'family': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['birds.TaxonomicGroup']"}),
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
            'order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['birds.TaxonomicGroup']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['birds.TaxonomicGroup']"}),
            'subfamily': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'blank': 'True', 'to': u"orm['birds.TaxonomicGroup']"})
        },
        u'birds.taxonomicgroup': {
            'Meta': {'ordering': "['level__depth', 'relative_position']", 'object_name': 'TaxonomicGroup'},
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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