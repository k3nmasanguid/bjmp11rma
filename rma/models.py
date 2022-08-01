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
    suffix = models.CharField('Suffix',max_length=3, null=False, blank=True, choices=SUFFIX)
    gender =  models.CharField('Gender',max_length=6, choices=GENDER)
    civil_status = models.CharField('Civil status',max_length=9, choices=CIVIL_STATUS)
    date_of_birth = models.DateField()
    place_of_birth = Uppercase('Place of birth',max_length=200)
    cellphone_no  = models.CharField('Cellphone Number', max_length=12)
    height = models.CharField('Height (m)', max_length=3)
    weight = models.CharField('Weight (kg)', max_length=3)
    blood_type = Uppercase('Blood type',max_length=3, blank=True)
    tin = models.CharField('TIN', max_length=11, blank=True)
    pag_ibig = models.CharField('Pag-ibig No.', max_length=20, blank=True)
    philhealth = models.CharField('Philhealth No.', max_length=14, blank=True)
    sss = models.CharField('SSS No.', max_length=12, blank=True)
    gsis = models.CharField('GSIS/BP No.', max_length=15, blank=True)

    class Meta:
        verbose_name_plural = "Personal Information"

    def __str__(self):
        return self.user.email

class PresentAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    region = models.CharField('Region', max_length=10)
    zip_code = models.CharField('Zipe code', max_length=4)
    province = models.CharField('Province', max_length=50)
    city_municipality = models.CharField('City/Municipality', max_length=100)
    barangay = models.CharField('Barangay', max_length=50)
    house = models.CharField('House/Lot/Unit No./Street/Subdivision', max_length=150)

    class Meta:
        verbose_name_plural = "Present Address"

    def __str__(self):
        return self.user.email