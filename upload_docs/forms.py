from django import forms
from upload_docs.models import PDS, TOR 



class PDSForm(forms.ModelForm):
   
    class Meta:
        model = PDS 
        exclude = ('user',)
        widgets = {
            'pds': forms.FileInput(),
        }