from django.shortcuts import render

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
    return render(request, 'contact.html')

 #Creation d'une fonction pour la page A propos
def apropos(request):
    return render(request, 'apropos.html')

 #Creation d'une fonction pour la page Galerie
def galerie(request):
    return render(request, 'galerie.html')



