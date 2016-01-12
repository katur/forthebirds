# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0008_auto_20160112_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
