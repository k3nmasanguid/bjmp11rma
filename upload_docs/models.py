import os
from django.db import models
from authentication.models import User
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize= value.size
    
    if filesize > 5242880:
        raise ValidationError("The maximum file size that can be uploaded is 5MB")
    else:
        return 

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class PDS(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pds = models.FileField('Personal Data Sheet', upload_to = user_directory_path, validators=[validate_file_size,FileExtensionValidator( ['pdf'] )])
    uploaded_at = models.DateTimeField('Uploaded Date/Time', auto_now=True)

    class Meta:
        verbose_name_plural = "Personal Data Sheet"

    
    def filename(self):
        return os.path.basename(self.file.name)


    def __str__(self):
        return self.user.email

class TOR(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tor = models.FileField('Personal Data Sheet', upload_to = user_directory_path, validators=[validate_file_size,FileExtensionValidator( ['pdf'] )])
    uploaded_at = models.DateTimeField('Uploaded Date/Time', auto_now=True)

    class Meta:
        verbose_name_plural = "Transcript of Records"

    
    def filename(self):
        return os.path.basename(self.file.name)


    def __str__(self):
        return self.user.email