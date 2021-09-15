from django.http import response
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status
from .models import Playlist
from .serializers import PlaylistSerializer

class PlaylistTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('music/', include('music.urls')),
    ]

    def test_get_playlists(self):
        url = reverse('music:playlist-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

