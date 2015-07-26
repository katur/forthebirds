# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0023_auto_20150125_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpeakingProgram',
            fields=[
                ('creation_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='creations.Creation')),
            ],
            options={
                'ordering': ['-title'],
            },
            bases=('creations.creation',),
        ),
        migrations.AlterModelOptions(
            name='abafieldguideimage',
            options={'ordering': ['title'], 'verbose_name': 'ABA Field Guide Images'},
        ),
    ]
