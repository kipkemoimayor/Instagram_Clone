# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-19 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='images',
            field=models.IntegerField(),
        ),
    ]