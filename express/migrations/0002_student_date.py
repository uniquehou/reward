# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-05-19 02:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('express', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 5, 19, 2, 21, 26, 739662, tzinfo=utc), verbose_name='预定日期'),
        ),
    ]
