# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-16 04:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0011_auto_20171116_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='description_file',
            field=models.URLField(blank=True, null=True, verbose_name='Explanatory File'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='speaker_description',
            field=models.TextField(blank=True, null=True, verbose_name='Speaker Description'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='speaker_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Speaker Name'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='speaker_photo',
            field=models.URLField(blank=True, null=True, verbose_name='Speaker Photograph'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='talk_description',
            field=models.TextField(blank=True, null=True, verbose_name='Talk Description'),
        ),
    ]