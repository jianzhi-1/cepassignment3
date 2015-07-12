# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0014_auto_20150712_0542'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='rating',
            field=models.ForeignKey(related_name='recipe', blank=True, to='recipe.Rating', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='food',
            name='restaurant',
            field=models.ManyToManyField(related_name='recipe', null=True, to='recipe.Restaurant', blank=True),
            preserve_default=True,
        ),
    ]
