# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 18:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='creation_date')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-title',),
                'verbose_name': '\u0411\u043b\u043e\u0433',
                'verbose_name_plural': '\u0411\u043b\u043e\u0433\u0438',
            },
        ),
    ]