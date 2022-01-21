# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0004_auto_20140911_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('creation_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='creations.Creation', on_delete=django.db.models.deletion.CASCADE)),
                ('published_by', models.CharField(max_length=100, blank=True)),
                ('date_published', models.DateField(null=True, blank=True)),
                ('url', models.URLField(blank=True)),
                ('file', models.FileField(null=True, upload_to=b'articles', blank=True)),
                ('text', models.TextField(help_text=b'Use Markdown syntax for italics, bullets, etc. See <a href="http://www.darkcoding.net/software/markdown-quick-reference">a quick reference</a>, <a href="http://www.markdowntutorial.com/">a tutorial</a>, or practice <a href="http://dillinger.io/">here</a>. ', blank=True)),
            ],
            options={
            },
            bases=('creations.creation',),
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('creation_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='creations.Creation', on_delete=django.db.models.deletion.CASCADE)),
                ('url', models.URLField(blank=True)),
            ],
            options={
            },
            bases=('creations.creation',),
        ),
    ]
