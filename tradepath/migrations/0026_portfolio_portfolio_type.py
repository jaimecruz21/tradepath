# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-06 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradepath', '0025_auto_20180306_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='portfolio_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]