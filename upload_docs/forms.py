from django import forms
from upload_docs.models import PDS, TOR, CAV, Diploma, BirthCert, EligibilityDoc, MarriageCert, Sketch, Waiver



class PDSForm(forms.ModelForm):
   
    class Meta:
        model = PDS 
        exclude = ('user',)
        widgets = {
            'pds': forms.FileInput(),
        }


class TORForm(forms.ModelForm):
   
    class Meta:
        model = TOR 
        exclude = ('user',)
        widgets = {
            'tor': forms.FileInput(),
        }


class CAVForm(forms.ModelForm):

    class Meta:
        model = CAV 
        exclude = ('user',)
        widgets = {
            'cav': forms.FileInput(),
        }

class DiplomaForm(forms.ModelForm):

    class Meta:
        model = Diploma 
        exclude = ('user',)
        widgets = {
            'diploma': forms.FileInput(),
        }

class BirthCertForm(forms.ModelForm):

    class Meta:
        model = BirthCert 
        exclude = ('user',)
        widgets = {
            'birthcert': forms.FileInput(),
        }

class EligibilityDocForm(forms.ModelForm):

    class Meta:
        model = EligibilityDoc 
        exclude = ('user',)
        widgets = {
            'eligibility_doc': forms.FileInput(),
        }

class MarriageCertForm(forms.ModelForm):

    class Meta:
        model = MarriageCert 
        exclude = ('user',)
        widgets = {
            'marriage_cert': forms.FileInput(),
        }

class SketchForm(forms.ModelForm):

    class Meta:
        model = Sketch 
        exclude = ('user',)
        widgets = {
            'sketch': forms.FileInput(),
        }

class WaiverForm(forms.ModelForm):

    class Meta:
        model = Waiver 
        exclude = ('user',)
        widgets = {
            'waiver': forms.FileInput(),
        }