# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-31 05:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0004_auto_20171029_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
    ]
