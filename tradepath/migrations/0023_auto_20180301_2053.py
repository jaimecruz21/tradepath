# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-02 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradepath', '0022_auto_20180301_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='condition',
            name='entity',
            field=models.CharField(choices=[('portfolio', 'Portfolio'), ('allocation', 'Allocation'), ('trade', 'Trade'), ('investment', 'Investment'), ('counterparty', 'Counterparty')], default='TASK', max_length=50),
        ),
        migrations.AlterField(
            model_name='condition',
            name='condition_type',
            field=models.CharField(blank=True, choices=[('TASK', 'Task'), ('ACTIVITY', 'Activity'), ('APPROVAL', 'Approval'), ('CONFIRMATION', 'Confirmation')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='external_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
