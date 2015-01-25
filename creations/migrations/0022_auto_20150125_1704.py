# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0021_auto_20150125_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abafieldguideimage',
            name='filename',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
