
from accounts.views import (login_view, 
                            register_view, 
                            logout_view, 
                            user_profile, 
                            user_profile_update)

from django.urls import path

urlpatterns = [
	path(r'^profile/(?P<username>\w+)/$', user_profile, name='user_profile'),
    path(r'^profile/(?P<username>\w+)/edit/$', user_profile_update, name='user_profile_update'),
    path(r'^login/$', login_view, name='login'),
    path(r'^register/$', register_view, name='register'),
    path(r'^logout/$', logout_view, name='logout'),
    #Contact


]
 