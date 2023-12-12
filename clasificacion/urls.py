from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtistaViewSet, AlbumViewSet, CancionViewSet, GeneroViewSet

router = DefaultRouter()
router.register(r'artistas', ArtistaViewSet, basename='artista')
router.register(r'albumes', AlbumViewSet, basename='album')
router.register(r'canciones', CancionViewSet, basename='cancion')
router.register(r'generos', GeneroViewSet, basename='genero')

urlpatterns = [
    path('', include(router.urls)),
]