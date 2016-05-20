# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-20 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20160520_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio_text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fun_fact',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to=b'profile_pictures'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_nr',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.CharField(blank=True, choices=[(b'CONSULTANT', b'Consultant'), (b'PARTNER', b'Partner')], max_length=40),
        ),
    ]