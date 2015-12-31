# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0048_auto_20151226_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='radioprogram',
            name='duration',
            field=models.PositiveIntegerField(default=None, null=True, blank=True),
        ),
    ]
