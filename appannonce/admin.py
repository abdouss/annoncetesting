from django.contrib import admin

# Register your models here.
from .models import Annonce,Ville,Galerie,Category
class AnnonceAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('nom',)}
	search_fields =['nom','prix']
	list_filter =['created']
	list_display =['nom','prix','created']
	list_editable =['prix']

class catAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Galerie)
admin.site.register(Category,catAdmin)
admin.site.register(Annonce, AnnonceAdmin)
admin.site.register(Ville)
