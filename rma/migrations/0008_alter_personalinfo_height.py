# Generated by Django 4.0.6 on 2022-08-02 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rma', '0007_alter_personalinfo_height'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Height (m)'),
        ),
    ]
