# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0018_researchcategory_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='research',
            old_name='research_category',
            new_name='category',
        ),
    ]
