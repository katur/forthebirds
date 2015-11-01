# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0039_auto_20151101_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchcategory',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='creations.ResearchCategory', null=True),
        ),
    ]
