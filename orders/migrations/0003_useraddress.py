# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20170407_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=120)),
                ('street', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('zipcode', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.UserCheckout')),
            ],
        ),
    ]
