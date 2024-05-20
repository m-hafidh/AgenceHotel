from django.shortcuts import render , redirect
from . forms import ContactForm  #importation de notre formulaire contact
from django.http import HttpResponse
from django.http  import HttpResponseRedirect
from .models import Contact
from .import models
from django import forms

from .forms import testForm





# Create your views here.
def test(request):
  form = testForm()  # ajout d’un nouveau formulaire ici
  return render(request,'test.html',
          {'form': form})  # passe ce formulaire au gabarit

#Creation d'une fonction pour la page accueil
def home(request):
    return render(request, 'home.html')

    #Creation d'une fonction pour la page Login
def login(request):
    return render(request, 'login.html')


    #Creation d'une fonction pour la page Register
def register(request):
    return render(request, 'register.html')

       #Creation d'une fonction pour la page Register
def contact(request):
    submitted = False
    #on appelle  la ethode Poste pour l'envoie de formulaire 
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid(): #si le formulaire est valide, envoyer 
            form.save() #enrgister si il est valide 
            return HttpResponseRedirect("/") #redirection vers la page d'accueil 
        else:
            form = ContactForm
            if "submitted" in request.GET:
                submitted = True 
            context = {"form" : form }
    return render(request, "contact.html")

 #Creation d'une fonction pour la page A propos
def apropos(request):
    return render(request, 'apropos.html')

 #Creation d'une fonction pour la page Galerie
def galerie(request):
    return render(request, 'galerie.html')



