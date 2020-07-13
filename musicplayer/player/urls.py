from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path: /player/
    url(r'^$', views.index, name='index'),

    # path: /player/11/ playlist id - 11
    url(r'^(?P<playlist_id>[0-9]+)/$', views.get_playlist, name='get_playlist'),
]