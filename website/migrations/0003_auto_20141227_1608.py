# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_userprofile_awards'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(default='', help_text=b'Use Markdown syntax for italics, bullets, etc. See <a href="http://www.darkcoding.net/software/markdown-quick-reference">a quick reference</a>, <a href="http://www.markdowntutorial.com/">a tutorial</a>, or practice <a href="http://dillinger.io/">here</a>. ', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='blurb',
            field=models.TextField(default='', help_text=b'Use Markdown syntax for italics, bullets, etc. See <a href="http://www.darkcoding.net/software/markdown-quick-reference">a quick reference</a>, <a href="http://www.markdowntutorial.com/">a tutorial</a>, or practice <a href="http://dillinger.io/">here</a>. ', blank=True),
            preserve_default=False,
        ),
    ]
