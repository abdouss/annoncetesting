
# Create your views here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Annonce
from .forms import Annonceform
from django.urls import reverse_lazy

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        subject = form.cleaned_data['subject']
        contactemail = form.cleaned_data['contact_email']
        message = form.cleaned_data['message']
        try:
            send_mail(subject, message, contactemail, ['admin@hotmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('home')
    context = {"form": form}
    return render(request, "appannonce/contact.html", context)


class Home(TemplateView):

	template_name="appannonce/home.html"

class ListAnnonceNouveau(ListView):#lister les nouveaux annonces

	model         =Annonce
	template_name ="appannonce/listannonce.html"
	paginate_by   =15
	context_object_name = 'annonces'



	def get_queryset(self):
		return Annonce.objects.order_by('-created')

class DetailAnnonce(DetailView):

	model                =Annonce
	template_name        ="appannonce/detailannonce.html"
	context_object_name  ='annonce'



class CreateAnnonce(LoginRequiredMixin,CreateView):

	form_class       =Annonceform
	model            =Annonce
	template_name    ="appannonce/Formannonce.html"


	def get_success_url(self, *args, **kwargs):
	   return reverse('detailannonce',kwargs={'slug':self.object.slug})

from django.urls import reverse
class UpdateAnnonce(LoginRequiredMixin,UpdateView):

	form_class           =Annonceform
	model                =Annonce
	template_name        ="appannonce/Formannonce.html"

	success_url          =reverse_lazy ('detailannonce')


class DeleteAnnonce(LoginRequiredMixin,DeleteView):

	model            =Annonce
	success_url      =reverse_lazy("listannonce")




class ListAnnonce(ListView):#lister les annonce est on choisier la ville est categorie est type

	model         =Annonce
	template_name ="appannonce/listannonce.html"
	paginate_by   =15
	context_object_name = 'annonces'



	def get_queryset(self):
		return self.Annonce.objects.filter(ville__exact='villes').filter(category__exact="categorys").filter(typeannonce__exact="typeannonce")