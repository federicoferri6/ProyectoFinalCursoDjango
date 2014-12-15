# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='liquid',
            name='manufactured_date',
            field=models.DateField(default=datetime.datetime(2014, 12, 15, 0, 8, 48, 174164, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='liquid',
            name='shipped_date',
            field=models.DateField(default=datetime.datetime(2014, 12, 15, 0, 8, 57, 228978, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solid',
            name='manufactured_date',
            field=models.DateField(default=datetime.datetime(2014, 12, 15, 0, 9, 7, 167771, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solid',
            name='shipped_date',
            field=models.DateField(default=datetime.datetime(2014, 12, 15, 0, 9, 40, 181940, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
