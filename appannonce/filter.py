from .models import Annonce
import django_filters

class AnnonceFilter(django_filters.FilterSet):
    class Meta:
        model = Annonce
        fields = ['ville', 'categorie', 'typeannonce', ]