# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-06-22 01:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_auto_20200621_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='patreonthankyou',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patreonthankyou',
            name='modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
