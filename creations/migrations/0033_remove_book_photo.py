# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0032_book_cover_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='photo',
        ),
    ]
