from django.conf.urls import url,include
from views import login, register, logout

from OpenML.accounts import views

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--


]