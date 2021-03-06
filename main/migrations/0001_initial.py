# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-10 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('college', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('latfield', models.DecimalField(decimal_places=15, default=14.6549, max_digits=20)),
                ('longfield', models.DecimalField(decimal_places=15, default=121.0645, max_digits=20)),
                ('contact_number', models.CharField(blank=True, max_length=50)),
                ('tags', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('sex', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=10)),
                ('age', models.CharField(max_length=3)),
                ('image', models.FileField(upload_to='')),
                ('contact_me', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default=1, max_length=3)),
                ('contact_number', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('comments', models.CharField(blank=True, max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
