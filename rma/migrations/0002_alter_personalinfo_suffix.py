# Generated by Django 4.0.6 on 2022-07-30 04:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='suffix',
            field=models.CharField(blank=True, choices=[('JR', 'JR'), ('SR', 'SR'), ('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV')], default=datetime.datetime(2022, 7, 30, 4, 46, 20, 152047, tzinfo=utc), max_length=3, verbose_name='Suffix'),
            preserve_default=False,
        ),
    ]
