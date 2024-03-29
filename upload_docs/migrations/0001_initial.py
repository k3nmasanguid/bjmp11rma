# Generated by Django 4.0.6 on 2022-08-05 03:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import upload_docs.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PDS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pds', models.FileField(upload_to=upload_docs.models.user_directory_path, validators=[upload_docs.models.validate_file_size, django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='Personal Data Sheet')),
                ('uploaded_at', models.DateTimeField(auto_now=True, verbose_name='Uploaded Date/Time')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Personal Data Sheet',
            },
        ),
    ]
