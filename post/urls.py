from django.conf.urls import url

from django.urls import include, path

from .views import *

urlpatterns = [
     url('add/', post_create, name='post_create'),
     url('(?P<id>\d+)/update/', post_update, name='update'),
     url('(?P<id>\d+)/like/', post_like, name="like"),
     url('(?P<id>\d+)/delete/', post_delete, name='delete'),
     url('last-posts/', last_posts, name='last_posts'),
     url('top50/', top_50, name='top50'),
]
