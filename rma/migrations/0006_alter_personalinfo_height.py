# Generated by Django 4.0.6 on 2022-08-02 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rma', '0005_alter_personalinfo_cellphone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Height (m)'),
        ),
    ]
