# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-11 01:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(max_length=20)),
                ('os', models.CharField(max_length=20)),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requester', models.CharField(max_length=20)),
                ('costcenter', models.CharField(max_length=20)),
                ('project', models.CharField(max_length=20)),
                ('owner', models.EmailField(max_length=254)),
                ('label', models.CharField(max_length=20)),
                ('order_date', models.DateTimeField(verbose_name='date ordered')),
            ],
        ),
        migrations.AddField(
            model_name='order_details',
            name='orders',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mhdb.Orders'),
        ),
    ]
