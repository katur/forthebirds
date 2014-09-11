# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('absolute_position', models.PositiveSmallIntegerField(null=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('common_name', models.CharField(max_length=50)),
                ('is_hidden', models.BooleanField(default=False)),
                ('blurb', models.TextField(help_text=b'Use Markdown syntax for italics, bullets, etc. See <a href="http://www.darkcoding.net/software/markdown-quick-reference">a quick reference</a>, <a href="http://www.markdowntutorial.com/">a tutorial</a>, or practice <a href="http://dillinger.io/">here</a>. ', blank=True)),
                ('main_photo_url', models.TextField(blank=True)),
                ('bird_of_the_week_name', models.CharField(max_length=50, blank=True)),
                ('french_name', models.CharField(max_length=50)),
                ('nacc_is_accidental', models.NullBooleanField()),
                ('nacc_is_hawaiian', models.NullBooleanField()),
                ('nacc_is_introduced', models.NullBooleanField()),
                ('nacc_is_nonbreeding', models.NullBooleanField()),
                ('nacc_is_extinct', models.NullBooleanField()),
                ('nacc_is_misplaced', models.NullBooleanField()),
                ('nacc_annotation', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['absolute_position'],
                'verbose_name_plural': 'bird species',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MinnesotaSpecies',
            fields=[
                ('species', models.OneToOneField(primary_key=True, serialize=False, to='birds.Species')),
                ('include_in_book', models.NullBooleanField(default=None)),
                ('mou_status', models.CharField(max_length=50, verbose_name=b'MOU status', blank=True)),
                ('mou_breeding_status', models.NullBooleanField(default=None, verbose_name=b'MOU breeding status')),
                ('mou_annotation', models.CharField(max_length=500, verbose_name=b'MOU annotation', blank=True)),
                ('range_in_minnesota', models.CharField(max_length=500, blank=True)),
                ('miscellaneous_notes', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['species__absolute_position'],
                'verbose_name_plural': 'Minnesota species',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaxonomicGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('common_name', models.CharField(max_length=50, blank=True)),
                ('relative_position', models.PositiveSmallIntegerField(null=True)),
            ],
            options={
                'ordering': ['level__depth', 'relative_position'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaxonomicLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('depth', models.PositiveSmallIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='taxonomicgroup',
            name='level',
            field=models.ForeignKey(to='birds.TaxonomicLevel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='taxonomicgroup',
            name='parent',
            field=models.ForeignKey(blank=True, to='birds.TaxonomicGroup', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='species',
            name='parent',
            field=models.ForeignKey(to='birds.TaxonomicGroup'),
            preserve_default=True,
        ),
    ]
