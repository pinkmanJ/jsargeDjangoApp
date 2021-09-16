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
            'songs': {'required': False}, # playlist doesn't have to have songs in it
        }

    # attaches user to playlist object on creation
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)    

class SongSerializer(ModelSerializer):
     
    playlists = PlaylistSerializer(many=True, read_only=True)

    class Meta:
        ordering = ['-id']
        model = Song
        fields = [
            'id',
            'name',
            'playlists',
        ]

        extra_kwargs = {
            'playlists': {'required': False}, # songs don't need to be in a playlist to exist
        }

    # attaches user to song object on creation (maybe not needed)
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)   