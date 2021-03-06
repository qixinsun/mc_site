# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-09 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportDataImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='File', verbose_name='车辆类型')),
            ],
            options={
                'verbose_name_plural': '导入车辆详细图片',
                'verbose_name': '导入车辆详细图片',
                'ordering': ['file'],
            },
        ),
    ]
