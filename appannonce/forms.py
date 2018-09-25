from __future__ import unicode_literals
from django import forms

from .models import Annonce,Galerie
import datetime
class Annonceform(forms.ModelForm):
	
	image   =forms.ModelChoiceField(queryset=Galerie.objects.all())
	created =forms.DateField(initial=datetime.date.today)



	class Meta:
		model =Annonce

		fields =('nom','prix','ville','description','categorie','typeannonce','caractéristiques','lieuaproximité','phone',"slug")



class ContactForm(forms.Form):
    subject = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True, label='email')
    message = forms.CharField(
        required=True,
        widget=forms.Textarea
        )
