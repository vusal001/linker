from django.conf.urls import url

from django.urls import include, path

from .views import *

urlpatterns = [
     url('login/', loginview, name='login'),
     url('register/', registerview, name='register'),
     url(r'^(?P<username>.+)/$', profil, name='profile'),
]
