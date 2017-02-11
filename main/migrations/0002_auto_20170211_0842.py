# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-11 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageProcessor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='doctor',
            name='latfield',
            field=models.DecimalField(decimal_places=15, default=None, max_digits=20),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='longfield',
            field=models.DecimalField(decimal_places=15, default=None, max_digits=20),
        ),
    ]