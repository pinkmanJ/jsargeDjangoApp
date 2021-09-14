from music.serializers import SongSerializer
from music.serializers import PlaylistSerializer
from django.db.models.query import QuerySet
from rest_framework.viewsets import ModelViewSet
from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

#from music.models import Artist
#from music.models import Album
from music.models import Song, Playlist

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the music index.")
    # we could pull data from database
    # transform data and send it 
    # serve template (which is an HTML page)
    # send out email

def songs(request):
    list_of_strings = Song.objects.all().values_list("name", flat=True)
    template = loader.get_template('music/index.html')
    context = {
        'list_of_strings': list_of_strings,
    }
    return HttpResponse(template.render(context, request))
    #return HttpResponse( "".join(list_of_strings))
    

def detail(request, artist_id):
    return HttpResponse("You're looking at artist %s." % artist_id)

def getAlbums(request, artist_id):
    return HttpResponse("You're looking at artist %s albums" % artist_id)    

def getSongs(request, artist_id):
    return HttpResponse("You're looking at artist %s songs" % artist_id)

class PlaylistViewSet(ModelViewSet):          
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    