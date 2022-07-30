from django.db import models
from authentication.models import User


class Uppercase(models.CharField):
    def to_python(self, value): 
        return value.upper()

GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
)

CIVIL_STATUS = (
        ('SINGLE', 'SINGLE'),
        ('MARRIED', 'MARRIED'),
        ('WIDOWED', 'WIDOWED'),
        ('SEPARATED', 'SEPARATED'),
        ('DIVORCED', 'DIVORCED'),
)

SUFFIX = (
        ('JR', 'JR'),
        ('SR', 'SR'),
        ('I', 'I'),
        ('II', 'II'),
        ('III', 'III'),
        ('IV', 'IV'),
)

class PersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = Uppercase('Last name',max_length=200)
    first_name = Uppercase('First name',max_length=200)
    middle_name = Uppercase('Middle name',max_length=200, blank=True)
    suffix = Uppercase('Suffix',max_length=3, null=False, blank=True, choices=SUFFIX)
    gender =  Uppercase('Gender',max_length=6, choices=GENDER)
    civil_status = Uppercase('Civil status',max_length=9, choices=CIVIL_STATUS)
    date_of_birth = models.DateField()
    place_of_birth = Uppercase('Place of birth',max_length=200)
    cellphone_no  = Uppercase('Cellphone Number', max_length=12)
    height = Uppercase('Height (m)', max_length=3)
    weight = Uppercase('Weight (kg)', max_length=3)
    blood_type = Uppercase('Blood type',max_length=3, blank=True)
    tin = Uppercase('TIN', max_length=11, blank=True)
    pag_ibig = Uppercase('Pag-ibig No.', max_length=20, blank=True)
    philhealth = Uppercase('Philhealth No.', max_length=14, blank=True)
    sss = Uppercase('SSS No.', max_length=12, blank=True)
    gsis = Uppercase('GSIS/BP No.', max_length=15, blank=True)

    class Meta:
        verbose_name_plural = "Personal Information"

    def __str__(self):
        return self.user.email

