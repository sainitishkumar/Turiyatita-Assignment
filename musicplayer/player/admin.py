from django.contrib import admin
from .models import Playlists, Song

admin.site.register(Playlists)
admin.site.register(Song)