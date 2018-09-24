from django.contrib import admin

# Register your models here.
from .models import Annonce,Galerie
class AnnonceAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('nom',)}
	search_fields =['nom','prix']
	list_filter =['created']
	list_display =['nom','prix','created']
	list_editable =['prix']



admin.site.register(Galerie)
admin.site.register(Annonce, AnnonceAdmin)
