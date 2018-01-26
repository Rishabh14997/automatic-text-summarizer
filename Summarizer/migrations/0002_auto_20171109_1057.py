# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-09 05:27
from __future__ import unicode_literals

import Summarizer.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Summarizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getfile',
            name='file',
            field=models.FileField(upload_to='documents/%Y/%m/%d/', validators=[Summarizer.validators.validate_file_extension]),
        ),
    ]