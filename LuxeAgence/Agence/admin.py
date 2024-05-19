from django.contrib import admin
from .models import Contact

# Register your models here.
#on enrgistre les contactes qu'on a creer

class ContactAdmin(admin.ModelAdmin):
    list_display = ("prenom","nom","email","objet","message") 
admin.site.register(Contact, ContactAdmin)



