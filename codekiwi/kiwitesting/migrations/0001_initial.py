# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, max_length=255, verbose_name='Surname')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('job', models.CharField(blank=True, max_length=255, null=True, verbose_name='Job Position')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Price')),
                ('vat', models.IntegerField(blank=True, null=True, verbose_name='Vat')),
            ],
        ),
        migrations.CreateModel(
            name='ProductQuestionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_biscuit', models.BooleanField(default=False, verbose_name='Biscuit?')),
                ('is_coated_in_chocolate', models.BooleanField(default=False, verbose_name='Coated in Chocolate?')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kiwitesting.Product', verbose_name='Product')),
            ],
        ),
    ]
