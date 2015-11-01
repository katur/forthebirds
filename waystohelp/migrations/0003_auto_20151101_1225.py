# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waystohelp', '0002_waytohelp_background_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waytohelp',
            name='background_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='website.UploadedImage', null=True),
        ),
    ]
