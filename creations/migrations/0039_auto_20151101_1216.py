# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0038_auto_20151101_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='website.UploadedImage', null=True),
        ),
    ]
