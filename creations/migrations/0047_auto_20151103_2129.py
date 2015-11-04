# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import private_media.storages


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0046_auto_20151101_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='externalproject',
            name='url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='speakingprogramfile',
            name='file',
            field=models.FileField(default=1, storage=private_media.storages.PrivateMediaStorage(), upload_to=b'speaking'),
            preserve_default=False,
        ),
    ]
