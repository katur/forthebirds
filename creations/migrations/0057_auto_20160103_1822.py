# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0056_auto_20160103_1810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publisher',
            new_name='published_by',
        ),
    ]
