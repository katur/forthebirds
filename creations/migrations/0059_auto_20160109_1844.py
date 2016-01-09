# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0058_auto_20160103_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radioprogram',
            name='duration',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
