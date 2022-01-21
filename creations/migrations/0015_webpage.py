# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0014_auto_20141230_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebPage',
            fields=[
                ('creation_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='creations.Creation', on_delete=django.db.models.deletion.CASCADE)),
                ('slug', models.SlugField(max_length=255, editable=False)),
                ('content', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['title'],
            },
            bases=('creations.creation',),
        ),
    ]
