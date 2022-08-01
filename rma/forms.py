from dataclasses import fields
from django import forms
from rma.models import PersonalInfo, PresentAddress


GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
)

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = '__all__'

    user = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))
    gender = forms.CharField(required=True, widget=forms.RadioSelect(choices=GENDER),)
    
class PresentAddressForm(forms.ModelForm):
    class Meta:
        model = PresentAddress
        fields = '__all__'

    user = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))