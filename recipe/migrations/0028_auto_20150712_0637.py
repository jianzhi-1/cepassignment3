# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0027_auto_20150712_0613'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='color',
            field=models.CharField(default=b'yellow', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='food',
            name='fontcolor',
            field=models.CharField(default=b'black', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rating',
            name='color',
            field=models.CharField(default=b'red', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rating',
            name='fontcolor',
            field=models.CharField(default=b'black', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='color',
            field=models.CharField(default=b'purple', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='fontcolor',
            field=models.CharField(default=b'white', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='food',
            name='restaurant',
            field=models.ManyToManyField(related_name='recipe', null=True, to='recipe.Restaurant', blank=True),
            preserve_default=True,
        ),
    ]
