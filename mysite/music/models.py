from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=300)

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)    