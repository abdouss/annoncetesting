from django.contrib import admin

# Register your models here.
from .models import Annonce,Ville,Galerie,Category
class AnnonceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nom',)}

admin.site.register(Annonce, AnnonceAdmin)
admin.site.register(Galerie)
admin.site.register(Category)