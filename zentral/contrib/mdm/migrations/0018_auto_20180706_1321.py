# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-07-06 13:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0039_auto_20180704_1049'),
        ('mdm', '0017_mdmenrollmentpackage'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='mdmenrollmentpackage',
            unique_together=set([('meta_business_unit', 'builder')]),
        ),
    ]
