from __future__ import unicode_literals
from django import forms

from .models import Annonce,Category

class Annonceform(forms.ModelForm):
	cat = forms.ModelChoiceField(queryset=Category.objects.all())

	class Meta:
		model =Annonce
		fields ='__all__'  



class ContactForm(forms.Form):
    subject = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True, label='email')
    message = forms.CharField(
        required=True,
        widget=forms.Textarea
        )
