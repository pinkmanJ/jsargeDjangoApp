from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
#class Artist(models.Model):
 #   name = models.CharField(max_length=255)
  #  age = models.IntegerField()
    
   # def __str__(self):
    #    return self.name

#class Album(models.Model):
 #   artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
  #  name = models.CharField(max_length=255)
   # description = models.TextField()

class Song(models.Model):
    #album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)   

class Playlist(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='playlists', on_delete=models.CASCADE)
    songs = models.ManyToManyField('Song', related_name='playlists', blank=True)
         