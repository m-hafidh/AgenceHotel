
from django import views
from django.urls import path,include
from.views import *
from . import views
from django.contrib import admin

urlpatterns = [
    #path('', include('Contact.urls')),
    path('admin/', admin.site.urls),
    
    path('contact/', views.contact, name="contact"),#la vue de la page contact

    path('', home, name="home"), #la vue de lan page d'accueil
    path('login', login, name="login"),#la vue de lan page login
    path('register', register, name="register"),#la vue de la page register
    #path('contact', contact, name="contact"),#la vue de la page contact
    path('apropos', apropos, name="apropos"),#la vue de la page a propos
    path('galerie', galerie, name="galerie"),#la vue de la page galerie
    path('visiter', visiter, name="visiter"),#la vue de la page visiter (page1)
    
]
