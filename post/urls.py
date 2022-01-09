from django.conf.urls import url

from django.urls import include, path

from .views import *

urlpatterns = [
     url('add/', post_create, name='post_create'),
     url('(?P<id>\d+)/update/', post_update, name='update'),
     path('like/', like_unlike_post, name="like"),
     url('(?P<id>\d+)/delete/', post_delete, name='delete'),
     url('last-posts/', last_posts, name='last_posts'),
     url('premium-posts/', premium, name='premium'),
     url('top50/', top_50, name='top50'),
     url('telegram_posts/', telegram_posts, name='telegram_posts'),
     url('wp_posts/', wp_posts, name='wp_posts'),
     url('insta_posts/', insta_posts, name='insta_posts'),
     url('facebook_posts/', facebook_posts, name='facebook_posts'),
     url('youtube_posts/', youtube_posts, name='youtube_posts'),
     url('tiktok_posts/', tiktok_posts, name='tiktok_posts'),

]
