# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-05 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='getFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('file', models.FileField(upload_to='')),
                ('length', models.IntegerField()),
            ],
        ),
    ]