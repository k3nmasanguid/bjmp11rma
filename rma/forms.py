from dataclasses import fields
from django import forms
from django.core.validators import RegexValidator
from rma.models import PersonalInfo, PresentAddress, PermanentAddress, Spouse, Father, Mother, Sibling


GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
)

class PersonalInfoForm(forms.ModelForm):
    user = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))
    gender = forms.CharField(required=True, widget=forms.RadioSelect(choices=GENDER),)
    cellphone_no = forms.CharField(
        min_length=11,
        max_length=11,
        validators=[RegexValidator(r'^[0-9]*$', message="Only number is allowed")],
        # validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message="Only letters is allowed")],
        widget=forms.TextInput(attrs={'data-mask':'0000-0000000','autocomplete':'off'}),
    )
    height = forms.DecimalField(
        max_digits=3,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'placeholder':'(e.g. 1.72)'}),
        # validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message="Only letters is allowed")],
    )
    weight = forms.CharField(
        max_length=3,
        min_length=2,
        validators=[RegexValidator(r'^[0-9]*$', message="Only number is allowed")],
        # validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', message="Only letters is allowed")],
    )
    class Meta:
        model = PersonalInfo
        fields = '__all__'


    
class PresentAddressForm(forms.ModelForm):
    class Meta:
        model = PresentAddress
        fields = '__all__'

    user = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))

class PermanentAddressForm(forms.ModelForm):
    class Meta:
        model = PermanentAddress
        fields = '__all__'

    user = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))



class SpouseForm(forms.ModelForm):
    user = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))
    gender = forms.CharField(required=True, widget=forms.RadioSelect(choices=GENDER),)

    class Meta:
        model = Spouse
        fields = '__all__'



class FatherForm(forms.ModelForm):
    user = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))

    class Meta:
        model = Father
        fields = '__all__'


class MotherForm(forms.ModelForm):
    user = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))

    class Meta:
        model = Mother
        fields = '__all__'

class SiblingForm(forms.ModelForm):
    # user = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))
    gender = forms.CharField(required=True, widget=forms.RadioSelect(choices=GENDER),)
    class Meta:
        model = Sibling
        exclude = ('user',)