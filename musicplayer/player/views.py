from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Playlists

from django.shortcuts import render

# Create your views here.
def index(request):
    playlists = Playlists.objects.all()
    context = {
        'playlists': playlists,
    }
    return render(request, 'player/index.html', context)

def get_playlist(request, playlist_id):
    try:
        plist = Playlists.objects.get(pk = playlist_id)
    except Playlists.DoesNotExist:
        raise Http404("no playlist with id: "+str(playlist_id))
    return render(request, 'player/details.html', {'playlist': plist})