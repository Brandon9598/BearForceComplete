# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-23 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0008_auto_20160719_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='type_of_shift_release',
            field=models.CharField(choices=[('null', 'null'), ('Permanent', 'Permanent shift release'), ('Temporary', 'Temporary shift release')], default='null', max_length=20),
        ),
        migrations.AlterField(
            model_name='shift',
            name='working_location',
            field=models.CharField(choices=[('Box Office', 'BO'), ('Main Desk', 'MD'), ('Fitness Center', 'FC'), ('Equipment Checkout', 'EC')], default='Main Desk', max_length=20),
        ),
    ]