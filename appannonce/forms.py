from __future__ import unicode_literals
from django import forms

from .models import Annonce 

class Annonceform(forms.ModelForm):

	class Meta:
		model =Annonce
		fields =('nom',"prix",'description','caractéristiques','lieuaproximité','slug','category','image','ville')   



class ContactForm(forms.Form):
    subject = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True, label='email')
    message = forms.CharField(
        required=True,
        widget=forms.Textarea
        )
