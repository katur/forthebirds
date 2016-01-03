# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0057_auto_20160103_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radioprogram',
            name='duration',
            field=models.PositiveIntegerField(default=45),
            preserve_default=False,
        ),
    ]
