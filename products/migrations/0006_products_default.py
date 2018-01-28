# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 18:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20170403_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='default',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_category', to='products.Category'),
        ),
    ]
