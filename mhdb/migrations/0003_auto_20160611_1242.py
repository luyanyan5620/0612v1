# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-11 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mhdb', '0002_auto_20160611_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='device_seri_number',
            field=models.IntegerField(),
        ),
    ]
