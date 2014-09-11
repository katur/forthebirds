# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field species on 'Creation'
        m2m_table_name = db.shorten_name(u'creations_creation_species')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('creation', models.ForeignKey(orm[u'creations.creation'], null=False)),
            ('species', models.ForeignKey(orm[u'birds.species'], null=False))
        ))
        db.create_unique(m2m_table_name, ['creation_id', 'species_id'])


    def backwards(self, orm):
        # Removing M2M table for field species on 'Creation'
        db.delete_table(db.shorten_name(u'creations_creation_species'))


    models = {
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
        },
        u'creations.book': {
            'Meta': {'ordering': "['-date_published']", 'object_name': 'Book', '_ormbases': [u'creations.Creation']},
            u'creation_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['creations.Creation']", 'unique': 'True', 'primary_key': 'True'}),
            'date_published': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'isbn_10': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'isbn_13': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'purchase_url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'year_published': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'creations.creation': {
            'Meta': {'object_name': 'Creation'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'species': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['birds.Species']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'creations.radioprogram': {
            'Meta': {'ordering': "['-original_air_date']", 'object_name': 'RadioProgram', '_ormbases': [u'creations.Creation']},
            u'creation_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['creations.Creation']", 'unique': 'True', 'primary_key': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'original_air_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'supplemental_content_url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'transcript': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['creations']