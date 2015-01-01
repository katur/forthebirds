# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0015_webpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='date_published',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='webpage',
            name='content',
            field=models.TextField(help_text=b'Use Markdown syntax for italics, bullets, etc. See <a href="http://www.darkcoding.net/software/markdown-quick-reference">a quick reference</a>, <a href="http://www.markdowntutorial.com/">a tutorial</a>, or practice <a href="http://dillinger.io/">here</a>. ', blank=True),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]
