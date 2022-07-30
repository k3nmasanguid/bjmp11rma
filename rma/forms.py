from dataclasses import fields
from django import forms
from rma.models import PersonalInfo


GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
)

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = '__all__'

    gender = forms.CharField(required=True, widget=forms.RadioSelect(choices=GENDER),)
    