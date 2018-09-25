
from appannonce.views import (contact,listerchoix)
from django.urls import re_path
from appannonce import views

urlpatterns = [

	re_path(r'^contact/$',contact, name='contact'),
    re_path(r'^listchoix/$',listerchoix, name='listerchoix'),

    re_path(r'^home/$',views.Home.as_view(),name='home'),
    re_path(r'^$',views.ListAnnonceNouveau.as_view(),name='listannonce'),
    re_path(r'^detail/(?P<slug>[\w-]+)/$',views.DetailAnnonce.as_view(),name='detailannonce'),
    re_path(r'^annonce/new/$',views.CreateAnnonce.as_view(),name='annoncenew'),
    re_path(r'^annonce/(?P<slug>[\w-]+)/edit/$',views.UpdateAnnonce.as_view(),name='edit'),
    re_path(r'^annonce/(?P<slug>[\w-]+)/remove/$',views.DeleteAnnonce.as_view(),name='delete'),
]
 