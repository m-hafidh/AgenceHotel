from django.shortcuts import render , redirect
from . forms import ContactForm  #importation de notre formulaire contact
from django.http import HttpResponse
from django.http  import HttpResponseRedirect
from .models import Contact
from .import models
from django import forms







# Create your views here.

#Creation d'une fonction pour la page accueil (envoyer les informations a la base de données )
def home(request):
    if request.method=="POST":
        contact=Contact()
        prenom=request.POST.get("prenom")
        nom=request.POST.get("nom")
        email=request.POST.get("email")
        objet=request.POST.get("objet")
        message=request.POST.get("message")

        contact.prenom=prenom
        contact.nom=nom
        contact.email=email
        contact.objet=objet
        contact.message=message
        contact.save()
        return HttpResponse("<h1> Merci de nous avoir contactez </h1>")
        
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

#Creation d'une fonction pour la page visiter (page1)
def visiter(request):
    return render(request, 'visiter.html')



