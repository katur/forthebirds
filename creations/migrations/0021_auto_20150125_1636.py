# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0020_abafieldguideimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abafieldguideimage',
            options={'ordering': ['filename']},
        ),
        migrations.RenameField(
            model_name='abafieldguideimage',
            old_name='filepath',
            new_name='filename',
        ),
    ]
