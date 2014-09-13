# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0006_auto_20140912_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='research',
            name='attribution',
            field=models.CharField(default='', max_length=200, blank=True),
            preserve_default=False,
        ),
    ]
