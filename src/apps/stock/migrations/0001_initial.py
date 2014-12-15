# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Liquid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('expirecy_date', models.DateField()),
                ('size', models.IntegerField()),
                ('label', models.ForeignKey(to='stock.Label')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Solid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('expirecy_date', models.DateField()),
                ('weight', models.IntegerField()),
                ('package_type', models.IntegerField(blank=True, choices=[(1, b'Nylon'), (2, b'Paper'), (3, b'Sealed')])),
                ('label', models.ForeignKey(to='stock.Label')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
