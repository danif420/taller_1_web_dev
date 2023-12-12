from clasificacion.models import Artista,Album,Cancion,Genero
from rest_framework import serializers


class ArtistaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artista
        fields = ['nombre','edad','trayectoria','photo']


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ['artista','titulo','fecha','photo']
        
class CancionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cancion
        fields = ['album','genero','titulo']


class GeneroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genero
        fields = ['nombre']