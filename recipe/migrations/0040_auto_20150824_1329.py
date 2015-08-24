# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0039_auto_20150818_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='picture',
            field=models.ImageField(default=b'/media/images/1.png', upload_to=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='food',
            name='restaurant',
            field=models.ManyToManyField(related_name='recipe', null=True, to='recipe.Restaurant', blank=True),
            preserve_default=True,
        ),
    ]
