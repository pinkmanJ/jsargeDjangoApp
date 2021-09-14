from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
#router.register(r'playlists', views.PlaylistViewSet)
router.register(r'api/playlists', views.PlaylistViewSet)
router.register(r'api/songs', views.SongViewSet)

urlpatterns = [
    path('', views.index),
    path('getSongs', views.songs),
    path('<int:artist_id>/', views.detail, name='detail'),
    path('<int:artist_id>/albums/', views.getAlbums, name='getAlbums'),
    path('<int:artist_id>/songs/', views.getSongs, name='getSongs'),
    path(r'', include(router.urls)),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework')),
]