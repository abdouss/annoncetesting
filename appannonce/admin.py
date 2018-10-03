from django.contrib import admin

# Register your models here.
from .models import Annonce,Galerie
class AnnonceAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('nom',)}
	search_fields =['nom','prix']
	list_filter =['created']
	list_display =['nom','prix','created']
	list_editable =['prix']

class GalerieAdmin(admin.ModelAdmin):

    readonly_fields = ["image"]

    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.headshot.url,
            width=obj.headshot.width,
            height=obj.headshot.height,
            )
    )



admin.site.register(Galerie,GalerieAdmin)
admin.site.register(Annonce, AnnonceAdmin)
