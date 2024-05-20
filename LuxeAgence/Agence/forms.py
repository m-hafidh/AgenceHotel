from django import forms
from django.forms import ModelForm
from . import models

from . models import Contact


class testForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("prenom","nom","email","objet","message",)


        widgets = {
            "prenom" : forms.TextInput(),
            "nom" : forms.TextInput(),
            "email" : forms.TextInput(),
            "objet" : forms.TextInput(),
            "message" : forms.TextInput()
        }


