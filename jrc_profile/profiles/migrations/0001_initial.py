# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_id', models.BigIntegerField()),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone_nr', models.CharField(max_length=40)),
                ('bio_text', models.TextField()),
                ('fun_fact', models.TextField()),
                ('active', models.BooleanField()),
            ],
        ),
    ]
