# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-19 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lucid', '0002_auto_20160920_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Date Created'),
        ),
    ]
