# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-12 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usercenter', '0005_auto_20180713_0109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payrecord',
            old_name='car_price',
            new_name='car',
        ),
        migrations.AlterField(
            model_name='payrecord',
            name='is_paied',
            field=models.BooleanField(default=True, verbose_name='是否付清'),
        ),
    ]
