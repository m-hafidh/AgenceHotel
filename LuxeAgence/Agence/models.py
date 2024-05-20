from django.db import models
from django.contrib import admin  #importation de l'admin


# Create your models here.

# on ecree notre model contact

class Contact (models.Model):
    prenom = models.CharField (max_length=200)
    nom = models.CharField (max_length=200)
    email = models.CharField (max_length=255)
    objet = models.CharField (max_length=200)
    message = models.CharField (max_length=10000)
    #date = models.DateTimeField(auto_now=True)

    #creeons un autre class pour la visualisation de l'admin
   # class ContactAdmin(admin.ModelAdmin):
       # list_display = ("prenom","nom","email","objet","message","date") 
    
    
    
