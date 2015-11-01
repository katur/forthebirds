# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_auto_20151018_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='main_photo',
            field=models.ForeignKey(related_name='main_uploaded_photo', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='website.UploadedImage', null=True),
        ),
    ]
