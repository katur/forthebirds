# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_remove_uploadedimage_image_again'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimage',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=website.models.get_updated_filename),
        ),
    ]
