# Generated by Django 4.0.6 on 2022-08-08 03:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import upload_docs.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('upload_docs', '0005_rename_tor_cav_cav'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diploma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diploma', models.FileField(upload_to=upload_docs.models.user_directory_path, validators=[upload_docs.models.validate_file_size, django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='Colege Diploma')),
                ('uploaded_at', models.DateTimeField(auto_now=True, verbose_name='Uploaded Date/Time')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'College Diploma',
            },
        ),
    ]