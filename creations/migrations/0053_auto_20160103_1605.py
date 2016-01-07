# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0052_auto_20160103_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=120),
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(max_length=120),
        ),
        migrations.AlterField(
            model_name='radioprogram',
            name='slug',
            field=models.SlugField(max_length=120),
        ),
        migrations.AlterField(
            model_name='research',
            name='slug',
            field=models.SlugField(max_length=120),
        ),
        migrations.AlterField(
            model_name='researchcategory',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
        migrations.AlterField(
            model_name='speakingprogram',
            name='slug',
            field=models.SlugField(max_length=120),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='slug',
            field=models.SlugField(max_length=120),
        ),
    ]
