# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0022_auto_20160211_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='scientific_name',
            field=models.CharField(max_length=50),
        ),
    ]
