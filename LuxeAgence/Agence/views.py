from django.shortcuts import render , redirect
from . forms import ContactForm  #importation de notre formulaire contact

# Create your views here.

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
    #on appelle  la ethode Poste pour l'envoie de formulaire 
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid(): #si le formulaire est valide, envoyer 
            form.save() #enrgister si il est valide 
            return redirect("base.html") #redirection vers la page d'accueil 
            form = ContactForm
            context = {"form" : form }
    return render(request, 'contact.html')

 #Creation d'une fonction pour la page A propos
def apropos(request):
    return render(request, 'apropos.html')

 #Creation d'une fonction pour la page Galerie
def galerie(request):
    return render(request, 'galerie.html')



