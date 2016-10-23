# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-01 01:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20160405_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.ManyToManyField(related_name='liked_blogs', to=settings.AUTH_USER_MODEL),
        ),
    ]
