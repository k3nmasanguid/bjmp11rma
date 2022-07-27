from django import forms
from django.contrib.auth.forms import UserCreationForm 
from authentication.models import User



class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','password1','password2')

class LoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        max_length=50,
        widget=forms.EmailInput
    )
    password = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput
    )