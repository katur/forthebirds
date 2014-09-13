# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0010_auto_20140912_2341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='research',
            old_name='category',
            new_name='research_category',
        ),
    ]
