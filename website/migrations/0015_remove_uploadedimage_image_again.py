# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_uploadedimage_image_again'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedimage',
            name='image_again',
        ),
    ]
