# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_uploadedimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='primary_photo',
            field=models.ImageField(null=True, upload_to=b'photos_of_laura', blank=True),
        ),
    ]
