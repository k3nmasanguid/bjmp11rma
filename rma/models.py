import datetime
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

LIVING_STATUS = (
        ('LIVING', 'LIVING'),
        ('DECEASED', 'DECEASED'),
        ('NOT KNOWN', 'NOT KNOWN'), 
)

ELEMENTARY_LEVEL = (
        ('GRADUATED', 'GRADUATED'),
        ('GRADE 1', 'GRADE 1'),
        ('GRADE 2', 'GRADE 2'),
        ('GRADE 3', 'GRADE 3'),
        ('GRADE 4', 'GRADE 4'),
        ('GRADE 5', 'GRADE 5'),
        ('GRADE 6', 'GRADE 6'),
)

HIGH_SCHOOL_LEVEL = (
        ('GRADUATED', 'GRADUATED'),
        ('GRADE 7', 'GRADE 7'),
        ('GRADE 8', 'GRADE 8'),
        ('GRADE 9', 'GRADE 9'),
        ('GRADE 10', 'GRADE 10'),
)

SENIOR_HIGH_LEVEL = (
        ('GRADUATED', 'GRADUATED'),
        ('GRADE 11', 'GRADE 11'),
        ('GRADE 12', 'GRADE 12'),
)

QUOTA_CHOICES = (
        ('Open', 'Open'),
        ('Close', 'Close'),
)

YEAR_CHOICES = [('N/A','N/A')]
for r in range(1990, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((str(r),str(r)))

class Quota(models.Model):
    batch = models.CharField('Batch Name', max_length=255, unique=True)
    status = models.CharField('Status', max_length=5, default='Close' ,choices = QUOTA_CHOICES)
    class Meta:
        verbose_name_plural = "Quota"

    def __str__(self):
        return self.batch



class PersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = Uppercase('Last name',max_length=200)
    first_name = Uppercase('First name',max_length=200)
    middle_name = Uppercase('Middle name',max_length=200, blank=True)
    suffix = Uppercase('Suffix',max_length=3, null=False, blank=True, choices=SUFFIX)
    gender =  Uppercase('Gender',max_length=6, choices=GENDER)
    civil_status = models.CharField('Civil status',max_length=9, choices=CIVIL_STATUS)
    date_of_birth = models.DateField()
    place_of_birth = Uppercase('Place of birth',max_length=200)
    cellphone_no  = models.CharField('Cellphone Number', max_length=11)
    height = models.DecimalField('Height (m)', max_digits=3, decimal_places=2)
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
    region = Uppercase('Region', max_length=10)
    zip_code = Uppercase('Zipe code', max_length=4)
    province = Uppercase('Province', max_length=50)
    city_municipality = Uppercase('City/Municipality', max_length=100)
    barangay = Uppercase('Barangay', max_length=50)
    house = Uppercase('House/Lot/Unit No./Street/Subdivision', max_length=150)

    class Meta:
        verbose_name_plural = "Present Address"

    def __str__(self):
        return self.user.email

class PermanentAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    region = Uppercase('Region', max_length=10)
    zip_code = Uppercase('Zipe code', max_length=4)
    province = Uppercase('Province', max_length=50)
    city_municipality = Uppercase('City/Municipality', max_length=100)
    barangay = Uppercase('Barangay', max_length=50)
    house = Uppercase('House/Lot/Unit No./Street/Subdivision', max_length=150)

    class Meta:
        verbose_name_plural = "Permanent Address"

    def __str__(self):
        return self.user.email

class Spouse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    living_status = Uppercase('Living Status',max_length=9, choices=LIVING_STATUS)
    last_name = Uppercase('Last name (Maiden)',max_length=200)
    first_name = Uppercase('First name',max_length=200)
    middle_name = Uppercase('Middle name',max_length=200, blank=True)
    suffix = Uppercase('Suffix',max_length=3, null=False, blank=True, choices=SUFFIX)
    gender =  models.CharField('Gender',max_length=6, choices=GENDER)

    class Meta:
        verbose_name_plural = "Spouse"

    def __str__(self):
        return self.user.email

class Father(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    living_status = Uppercase('Living Status',max_length=9, choices=LIVING_STATUS)
    last_name = Uppercase('Last name',max_length=200)
    first_name = Uppercase('First name',max_length=200)
    middle_name = Uppercase('Middle name',max_length=200, blank=True)
    suffix = Uppercase('Suffix',max_length=3, null=False, blank=True, choices=SUFFIX)

    class Meta:
        verbose_name_plural = "Father"

    def __str__(self):
        return self.user.email

class Mother(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    living_status = Uppercase('Living Status',max_length=9, choices=LIVING_STATUS)
    last_name = Uppercase('Last name (Maiden)',max_length=200)
    first_name = Uppercase('First name',max_length=200)
    middle_name = Uppercase('Middle name',max_length=200, blank=True)

    class Meta:
        verbose_name_plural = "Mother"

    def __str__(self):
        return self.user.email

class Sibling(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    living_status = Uppercase('Living Status',max_length=9, choices=LIVING_STATUS)
    last_name = Uppercase('Last name (Maiden)',max_length=200)
    first_name = Uppercase('First name',max_length=200)
    middle_name = Uppercase('Middle name',max_length=200, blank=True)
    suffix = Uppercase('Suffix',max_length=3, null=False, blank=True, choices=SUFFIX)
    gender =  models.CharField('Gender',max_length=6, choices=GENDER)
    civil_status = Uppercase('Civil status',max_length=9, choices=CIVIL_STATUS)

    class Meta:
        verbose_name_plural = "Sibling"

    def __str__(self):
        return self.user.email

class Children(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    living_status = Uppercase('Living Status',max_length=9, choices=LIVING_STATUS)
    last_name = Uppercase('Last name (Maiden)',max_length=200)
    first_name = Uppercase('First name',max_length=200)
    middle_name = Uppercase('Middle name',max_length=200, blank=True)
    suffix = Uppercase('Suffix',max_length=3, null=False, blank=True, choices=SUFFIX)
    gender =  models.CharField('Gender',max_length=6, choices=GENDER)
    date_of_birth = models.DateField()

    class Meta:
        verbose_name_plural = "Children"

    def __str__(self):
        return self.user.email

class Primary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school_name = Uppercase('Name of School', max_length=200)
    year_from = Uppercase('From',max_length=4, choices=YEAR_CHOICES)
    year_to = Uppercase('To',max_length=4, choices=YEAR_CHOICES)
    highest_level = Uppercase('Highest Level', max_length=50, choices=ELEMENTARY_LEVEL)
    year_graduated = Uppercase('Year Graduated',max_length=4, choices=YEAR_CHOICES)
    academic_honors = Uppercase('Academic Honors Received', max_length=150, blank=True, null=False)

    class Meta:
        verbose_name_plural = "Primary Education"

    def __str__(self):
        return self.user.email

class HighSchool(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school_name = Uppercase('Name of School', max_length=200)
    year_from = Uppercase('From',max_length=4, choices=YEAR_CHOICES)
    year_to = Uppercase('To',max_length=4, choices=YEAR_CHOICES)
    highest_level = Uppercase('Highest Level', max_length=50, choices=HIGH_SCHOOL_LEVEL)
    year_graduated = Uppercase('Year Graduated',max_length=4, choices=YEAR_CHOICES)
    academic_honors = Uppercase('Academic Honors Received', max_length=150, blank=True, null=False)

    class Meta:
        verbose_name_plural = "High School"

    def __str__(self):
        return self.user.email

class SeniorHigh(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school_name = Uppercase('Name of School', max_length=200)
    year_from = Uppercase('From',max_length=4, choices=YEAR_CHOICES)
    year_to = Uppercase('To',max_length=4, choices=YEAR_CHOICES)
    highest_level = Uppercase('Highest Level', max_length=50, choices=SENIOR_HIGH_LEVEL)
    year_graduated = Uppercase('Year Graduated',max_length=4, choices=YEAR_CHOICES)
    academic_honors = Uppercase('Academic Honors Received', max_length=150, blank=True, null=False)

    class Meta:
        verbose_name_plural = "Senior High"

    def __str__(self):
        return self.user.email

class College(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='college_rel')
    school_name = Uppercase('Name of School', max_length=200)
    course = Uppercase('Course/Degree', max_length=200)
    year_from = Uppercase('From',max_length=4, choices=YEAR_CHOICES)
    year_to = Uppercase('To',max_length=4, choices=YEAR_CHOICES)
    units_earned = models.DecimalField('Units Earned', max_digits=4, decimal_places=2, blank=True, null=True)
    year_graduated = Uppercase('Year Graduated',max_length=4, choices=YEAR_CHOICES)
    academic_honors = Uppercase('Academic Honors Received', max_length=150, blank=True, null=False)

    class Meta:
        verbose_name_plural = "College"

    def __str__(self):
        return self.user.email

class Graduate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school_name = Uppercase('Name of School', max_length=200)
    degree = Uppercase('Degree', max_length=200)
    year_from = Uppercase('From',max_length=4, choices=YEAR_CHOICES)
    year_to = Uppercase('To',max_length=4, choices=YEAR_CHOICES)
    units_earned = models.DecimalField('Units Earned', max_digits=4, decimal_places=2, blank=True, null=True)
    year_graduated = Uppercase('Year Graduated',max_length=4, choices=YEAR_CHOICES)
    academic_honors = Uppercase('Academic Honors Received', max_length=150, blank=True, null=False)

    class Meta:
        verbose_name_plural = "Graduate Studies"

    def __str__(self):
        return self.user.email


class Eligibility(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    eligibility = Uppercase('Eligibility', max_length=200)
    rating = models.DecimalField('Units Earned', max_digits=4, decimal_places=2)
    date_of_exam = models.DateField('Date of Examination/Conferment')
    place_of_exam = Uppercase('Place of Examination/Conferment', max_length=200, blank=True)
    license = Uppercase('License Number', max_length=50, blank=True)


    class Meta:
        verbose_name_plural = "Eligibility"

    def __str__(self):
        return self.user.email

