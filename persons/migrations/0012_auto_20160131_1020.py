# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0011_auto_20160131_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='CreatedBy',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='LastUpdatedBy',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
