# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 22:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_auto_20160920_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='next_photo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prev_photo', to='photos.Photo'),
        ),
    ]
