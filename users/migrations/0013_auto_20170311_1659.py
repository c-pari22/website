# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20170113_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewslot',
            name='date',
            field=models.DateTimeField(verbose_name='DateTime'),
        ),
        migrations.AlterField(
            model_name='interviewslot',
            name='day_of_week',
            field=models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], max_length=1, default=1),
        ),
    ]
