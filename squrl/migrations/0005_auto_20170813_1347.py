# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-13 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squrl', '0004_auto_20170813_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squrls',
            name='squrl',
            field=models.SlugField(primary_key=True, serialize=False),
        ),
    ]