# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0016_auto_20150101_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalProject',
            fields=[
                ('creation_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='creations.Creation')),
                ('url', models.URLField(blank=True)),
            ],
            options={
                'ordering': ['title'],
            },
            bases=('creations.creation',),
        ),
    ]
