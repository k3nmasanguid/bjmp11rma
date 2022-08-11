# Generated by Django 4.0.6 on 2022-08-10 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_user_batch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('Complete', 'Complete'), ('For Submission', 'For Submission'), ('Pending', 'Pending')], default='Pending', max_length=20, verbose_name='Application Status'),
        ),
    ]