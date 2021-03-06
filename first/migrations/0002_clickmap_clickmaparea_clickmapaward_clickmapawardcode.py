# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-05-06 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, verbose_name='名称')),
                ('img', models.ImageField(upload_to='clickmap', verbose_name='抽奖图片')),
                ('url', models.CharField(max_length=50, verbose_name='抽奖链接')),
            ],
            options={
                'verbose_name': '抽奖图片',
                'verbose_name_plural': '抽奖图片',
            },
        ),
        migrations.CreateModel(
            name='ClickMapArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='区域名')),
                ('area', models.CharField(max_length=50, verbose_name='抽奖区域')),
                ('img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.ClickMap', verbose_name='图片')),
            ],
            options={
                'verbose_name': '奖品区域',
                'verbose_name_plural': '奖品区域',
            },
        ),
        migrations.CreateModel(
            name='ClickMapAward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='奖品名')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.ClickMapArea', verbose_name='绑定区域')),
            ],
            options={
                'verbose_name': '奖品',
                'verbose_name_plural': '奖品',
            },
        ),
        migrations.CreateModel(
            name='ClickMapAwardCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='兑奖码')),
                ('use', models.CharField(choices=[('1', '已使用'), ('2', '未使用')], default='2', max_length=2, verbose_name='使用情况')),
                ('award', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.ClickMapAward', verbose_name='奖品')),
            ],
            options={
                'verbose_name': '兑奖码',
                'verbose_name_plural': '兑奖码',
            },
        ),
    ]
