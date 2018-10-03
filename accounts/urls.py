
from accounts.views import (login_view, 
                            register_view, 
                            logout_view, 
                            user_profile, 
                            user_profile_update)

from django.urls import re_path

urlpatterns = [
	re_path(r'^profile/(?P<username>\w+)/$', user_profile, name='user_profile'),
    re_path(r'^profile/(?P<username>\w+)/edit/$', user_profile_update, name='user_profile_update'),
    re_path(r'^login/$', login_view, name='login'),
    re_path(r'^register/$', register_view, name='register'),
    re_path(r'^logout/$', logout_view, name='logout'),
    #Contact

]
 