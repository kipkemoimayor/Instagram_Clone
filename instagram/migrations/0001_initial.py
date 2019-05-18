# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-18 07:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('name', models.CharField(max_length=30)),
                ('captiom', models.CharField(max_length=30)),
                ('likes', models.IntegerField()),
                ('comments', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('userId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(blank=True, upload_to='profile/')),
                ('bio', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.Profile'),
        ),
    ]