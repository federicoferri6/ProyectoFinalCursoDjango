# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20141215_0009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='liquid',
            old_name='expirecy_date',
            new_name='expiracy_date',
        ),
        migrations.RenameField(
            model_name='solid',
            old_name='expirecy_date',
            new_name='expiracy_date',
        ),
    ]
