# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Creation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('creation_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='creations.Creation')),
                ('purchase_url', models.CharField(max_length=500, blank=True)),
                ('photo', models.ImageField(null=True, upload_to=b'books', blank=True)),
                ('publisher', models.CharField(max_length=100, blank=True)),
                ('isbn_10', models.CharField(max_length=20, blank=True)),
                ('isbn_13', models.CharField(max_length=20, blank=True)),
                ('date_published', models.DateField(null=True, blank=True)),
                ('year_published', models.PositiveSmallIntegerField(null=True, blank=True)),
            ],
            options={
                'ordering': ['-date_published'],
            },
            bases=('creations.creation',),
        ),
        migrations.CreateModel(
            name='RadioProgram',
            fields=[
                ('creation_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='creations.Creation')),
                ('original_air_date', models.DateField(null=True, blank=True)),
                ('file', models.FileField(null=True, upload_to=b'radio', blank=True)),
                ('supplemental_content_url', models.CharField(max_length=500, blank=True)),
                ('transcript', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['-original_air_date'],
            },
            bases=('creations.creation',),
        ),
        migrations.AddField(
            model_name='creation',
            name='species',
            field=models.ManyToManyField(to='birds.Species'),
            preserve_default=True,
        ),
    ]
