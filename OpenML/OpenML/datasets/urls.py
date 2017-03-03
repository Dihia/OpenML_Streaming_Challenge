from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<id>[1-9][0-9]*)$', views.show, name='show'),
    url(r'^list$', views.index, name='index')
]
