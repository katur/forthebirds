# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0013_auto_20141227_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creation',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
