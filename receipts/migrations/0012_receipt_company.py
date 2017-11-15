# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 03:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_auto_20171113_1542'),
        ('receipts', '0011_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Company'),
        ),
    ]
