# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20141215_0019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('manufactured_date', models.DateField()),
                ('shipped_date', models.DateField()),
                ('expiracy_date', models.DateField()),
                ('weight', models.IntegerField()),
                ('package_type', models.IntegerField(blank=True, choices=[(1, b'Nylon'), (2, b'Paper'), (3, b'Sealed'), (4, b'Bottle')])),
                ('label', models.ForeignKey(to='stock.Label')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='liquid',
            name='label',
        ),
        migrations.DeleteModel(
            name='Liquid',
        ),
        migrations.RemoveField(
            model_name='solid',
            name='label',
        ),
        migrations.DeleteModel(
            name='Solid',
        ),
    ]
