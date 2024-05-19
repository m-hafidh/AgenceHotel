from django import forms
from django.forms import ModelForm

from . models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["prenom","nom","email","objet","message"]


        widgets = {
            "prenom" : forms.TextInput(),
            "nom" : forms.TextInput(),
            "email" : forms.TextInput(),
            "objet" : forms.TextInput(),
            "message" : forms.TextInput()
        }