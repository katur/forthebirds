# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0009_research_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='researchcategory',
            options={'ordering': ['name'], 'verbose_name_plural': 'research categories'},
        ),
        migrations.RenameField(
            model_name='researchcategory',
            old_name='category',
            new_name='name',
        ),
    ]
