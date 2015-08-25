# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0040_auto_20150824_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='picture',
            field=models.ImageField(default=b'mc.png', upload_to=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='food',
            name='picturename',
            field=models.CharField(default=b'mc', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='food',
            name='restaurant',
            field=models.ManyToManyField(related_name='recipe', null=True, to='recipe.Restaurant', blank=True),
            preserve_default=True,
        ),
    ]
