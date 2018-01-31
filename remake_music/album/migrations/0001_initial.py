# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 12:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.IntegerField(default=2017, verbose_name='year')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.Artist')),
            ],
        ),
    ]