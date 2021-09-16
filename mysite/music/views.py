from django.db import models
from music.serializers import SongSerializer
from music.serializers import PlaylistSerializer
from django.db.models.query import QuerySet
from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse

#from music.models import Artist
#from music.models import Album
from music.models import Song, Playlist

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the music index.")
    
# def detail(request, artist_id):
#     return HttpResponse("You're looking at artist %s." % artist_id)

# def getAlbums(request, artist_id):
#     return HttpResponse("You're looking at artist %s albums" % artist_id)    

# def getSongs(request, artist_id):
#     return HttpResponse("You're looking at artist %s songs" % artist_id)

class PlaylistViewSet(ModelViewSet):          
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    # override get_queryset if you need to return different sets based on request
    # this makes it so that a user can only view Playlists they created
    def get_queryset(self):
        user = self.request.user
        return Playlist.objects.filter(user=user)

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    