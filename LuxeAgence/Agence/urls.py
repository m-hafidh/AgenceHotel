
from django import views
from django.urls import path,include
from.views import *

urlpatterns = [
    path('', home, name="home"), #la vue de lan page d'accueil
    path('login', login, name="login"),#la vue de lan page login
    path('register', register, name="register"),#la vue de lan page register
    path('contact', contact, name="contact"),#la vue de lan page contact
]
