# Generated by Django 4.0.6 on 2022-08-16 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rma', '0003_alter_quota_status'),
        ('authentication', '0006_alter_user_batch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='batch',
            field=models.ManyToManyField(null=True, to='rma.quota'),
        ),
    ]