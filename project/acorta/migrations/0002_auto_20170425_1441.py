# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acorta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='urls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Url_corta', models.CharField(max_length=500)),
                ('Url_larga', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='url_a_acortar',
        ),
    ]
