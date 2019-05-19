# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-05-19 02:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('express', '0002_student_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='院系名')),
            ],
            options={
                'verbose_name': '院系',
                'verbose_name_plural': '院系',
            },
        ),
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 5, 19, 2, 31, 58, 325352, tzinfo=utc), verbose_name='预定日期'),
        ),
        migrations.AddField(
            model_name='grade',
            name='department',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, to='express.Department', verbose_name='所属院系'),
        ),
    ]