# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-06 13:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoplay', '0004_video'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Video',
        ),
    ]