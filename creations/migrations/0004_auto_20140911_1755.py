# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0003_remove_book_year_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn_10',
            field=models.CharField(max_length=20, verbose_name=b'ISBN 10', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn_13',
            field=models.CharField(max_length=20, verbose_name=b'ISBN 13', blank=True),
        ),
        migrations.AlterField(
            model_name='creation',
            name='description',
            field=models.TextField(help_text=b'Use Markdown syntax for italics, bullets, etc. See <a href="http://www.darkcoding.net/software/markdown-quick-reference">a quick reference</a>, <a href="http://www.markdowntutorial.com/">a tutorial</a>, or practice <a href="http://dillinger.io/">here</a>. ', blank=True),
        ),
        migrations.AlterField(
            model_name='radioprogram',
            name='transcript',
            field=models.TextField(help_text=b'Use Markdown syntax for italics, bullets, etc. See <a href="http://www.darkcoding.net/software/markdown-quick-reference">a quick reference</a>, <a href="http://www.markdowntutorial.com/">a tutorial</a>, or practice <a href="http://dillinger.io/">here</a>. ', blank=True),
        ),
    ]
