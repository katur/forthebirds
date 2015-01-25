# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0019_auto_20150104_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='ABAFieldGuideImage',
            fields=[
                ('creation_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='creations.Creation')),
                ('filepath', models.CharField(max_length=500, blank=True)),
            ],
            options={
                'ordering': ['filepath'],
            },
            bases=('creations.creation',),
        ),
    ]
