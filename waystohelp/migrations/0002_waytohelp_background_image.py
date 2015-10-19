# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_auto_20151018_1630'),
        ('waystohelp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='waytohelp',
            name='background_image',
            field=models.ForeignKey(blank=True, to='website.UploadedImage', null=True),
        ),
    ]
