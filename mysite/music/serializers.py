from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Playlist, Song, User

class PlaylistSerializer(ModelSerializer):
    
    
    class Meta:
        ordering = ['-id']
        model = Playlist
        fields = [
            'title',
            'id',
            'user',
            'songs',
        ]
        extra_kwargs = {
            'user': {'read_only': True},
            'songs': {'required': False}, # added this kwarg
        }

class SongSerializer(ModelSerializer):
    
    playlists = PlaylistSerializer(many=True, read_only=True)

    class Meta:
        ordering = ['-id']
        model = Song
        fields = [
            'id',
            #'album',
            'name',
            'playlists',
        ]

        extra_kwargs = {
            'playlists': {'required': False},
        }

    # think of validated data as a JSON body being POSTed
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    # update playlist

    # delete playlist

    # add song
    #def addSongToPlaylist():
        # give the title of the song
        # give the playlist id?
        # get playlist object
        # add song object to playlist songs field       