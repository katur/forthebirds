# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0045_auto_20151101_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radioprogram',
            name='file',
            field=models.FileField(default=1, upload_to=b'radio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='radioprogram',
            name='original_air_date',
            field=models.DateField(default=datetime.datetime(2015, 11, 1, 22, 42, 37, 119772, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
