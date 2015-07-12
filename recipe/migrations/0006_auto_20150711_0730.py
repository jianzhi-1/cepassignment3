# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_auto_20150711_0727'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='contact',
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='information',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
