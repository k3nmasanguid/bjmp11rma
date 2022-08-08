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
    tor = models.FileField('Transcript of Records', upload_to = user_directory_path, validators=[validate_file_size,FileExtensionValidator( ['pdf'] )])
    uploaded_at = models.DateTimeField('Uploaded Date/Time', auto_now=True)

    class Meta:
        verbose_name_plural = "Transcript of Records"
  
    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.user.email


class CAV(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cav = models.FileField('Certification, Authentication and Verification', upload_to = user_directory_path, validators=[validate_file_size,FileExtensionValidator( ['pdf'] )])
    uploaded_at = models.DateTimeField('Uploaded Date/Time', auto_now=True)

    class Meta:
        verbose_name_plural = "CAV"

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.user.email

class Diploma(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    diploma = models.FileField('College Diploma', upload_to = user_directory_path, validators=[validate_file_size,FileExtensionValidator( ['pdf'] )])
    uploaded_at = models.DateTimeField('Uploaded Date/Time', auto_now=True)

    class Meta:
        verbose_name_plural = "College Diploma"

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.user.email

class BirthCert(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthcert = models.FileField('Birth Certificate', upload_to = user_directory_path, validators=[validate_file_size,FileExtensionValidator( ['pdf'] )])
    uploaded_at = models.DateTimeField('Uploaded Date/Time', auto_now=True)

    class Meta:
        verbose_name_plural = "Birth Certificate"

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.user.email

class EligibilityDoc(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    eligibility_doc = models.FileField('Eligibility', upload_to = user_directory_path, validators=[validate_file_size,FileExtensionValidator( ['pdf'] )])
    uploaded_at = models.DateTimeField('Uploaded Date/Time', auto_now=True)

    class Meta:
        verbose_name_plural = "Eligibility"

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.user.email


class MarriageCert(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    marriage_cert = models.FileField('Marriage Certificate', upload_to = user_directory_path, validators=[validate_file_size,FileExtensionValidator( ['pdf'] )])
    uploaded_at = models.DateTimeField('Uploaded Date/Time', auto_now=True)

    class Meta:
        verbose_name_plural = "Marriage Certificate"

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.user.email

class Sketch(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sketch = models.FileField('Sketch of Residency/Locality', upload_to = user_directory_path, validators=[validate_file_size,FileExtensionValidator( ['pdf'] )])
    uploaded_at = models.DateTimeField('Uploaded Date/Time', auto_now=True)

    class Meta:
        verbose_name_plural = "Sketch of Residency"

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.user.email

class Waiver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    waiver = models.FileField('Certificate for Age and/or Height Waiver', upload_to = user_directory_path, validators=[validate_file_size,FileExtensionValidator( ['pdf'] )])
    uploaded_at = models.DateTimeField('Uploaded Date/Time', auto_now=True)

    class Meta:
        verbose_name_plural = "Certificate for Age and/or Height Waiver"

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.user.email


class Barangay(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    barangay = models.FileField('Barangay', upload_to = user_directory_path, validators=[validate_file_size,FileExtensionValidator( ['pdf'] )])
    uploaded_at = models.DateTimeField('Uploaded Date/Time', auto_now=True)

    class Meta:
        verbose_name_plural = "Barangay"

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.user.email

class NBI(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nbi = models.FileField('NBI', upload_to = user_directory_path, validators=[validate_file_size,FileExtensionValidator( ['pdf'] )])
    uploaded_at = models.DateTimeField('Uploaded Date/Time', auto_now=True)

    class Meta:
        verbose_name_plural = "NBI"

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.user.email


class Police(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    police = models.FileField('Police', upload_to = user_directory_path, validators=[validate_file_size,FileExtensionValidator( ['pdf'] )])
    uploaded_at = models.DateTimeField('Uploaded Date/Time', auto_now=True)

    class Meta:
        verbose_name_plural = "Police"

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.user.email

class Fiscal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fiscal = models.FileField('Fiscal', upload_to = user_directory_path, validators=[validate_file_size,FileExtensionValidator( ['pdf'] )])
    uploaded_at = models.DateTimeField('Uploaded Date/Time', auto_now=True)

    class Meta:
        verbose_name_plural = "Fiscal"

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.user.email

class MTC(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mtc = models.FileField('MTC', upload_to = user_directory_path, validators=[validate_file_size,FileExtensionValidator( ['pdf'] )])
    uploaded_at = models.DateTimeField('Uploaded Date/Time', auto_now=True)

    class Meta:
        verbose_name_plural = "MTC"

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.user.email

class RTC(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rtc = models.FileField('RTC', upload_to = user_directory_path, validators=[validate_file_size,FileExtensionValidator( ['pdf'] )])
    uploaded_at = models.DateTimeField('Uploaded Date/Time', auto_now=True)

    class Meta:
        verbose_name_plural = "RTC"

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.user.email

class PNPDI(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pnpdi = models.FileField('PNP Directorate for Intelligence Clearance', upload_to = user_directory_path, validators=[validate_file_size,FileExtensionValidator( ['pdf'] )])
    uploaded_at = models.DateTimeField('Uploaded Date/Time', auto_now=True)

    class Meta:
        verbose_name_plural = "PNP Directorate for Intelligence Clearance"

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.user.email

