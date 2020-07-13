from django.db import models

class Users(models.Model):
    user_name = models.CharField(max_length = 200)

class Playlists(models.Model):
    playlist_name = models.CharField(max_length = 200)
    playlist_owner = models.CharField(max_length = 200)
    def __str__(self):
        return "Playlist :" + self.playlist_name + ", Owned by: " + self.playlist_owner

class Song(models.Model):
    album = models.ForeignKey(Playlists, on_delete=models.CASCADE)
    song_name = models.CharField(max_length = 200)
    def __str__(self):
        return "Song name :" + self.song_name + ", in: " + self.album.playlist_name