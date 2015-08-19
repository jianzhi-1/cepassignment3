# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('recipe', '0035_auto_20150726_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='user',
            field=models.ForeignKey(blank=True, to='accounts.UserProfile', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='food',
            name='restaurant',
            field=models.ManyToManyField(related_name='recipe', null=True, to='recipe.Restaurant', blank=True),
            preserve_default=True,
        ),
    ]
