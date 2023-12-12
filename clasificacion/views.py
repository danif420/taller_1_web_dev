from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from clasificacion.models import Artista,Album,Cancion,Genero
from clasificacion.serializers import ArtistaSerializer,AlbumSerializer,CancionSerializer,GeneroSerializer
from django.urls import reverse_lazy
from rest_framework import permissions, views, status,viewsets
from rest_framework.response import Response
from django.contrib.auth import login
from django.http import JsonResponse
from . import serializers

class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({"str": "success"}, status=status.HTTP_202_ACCEPTED)

class ArtistaViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer
    def list(self, request, *args, **kwargs):
        response_data = super().list(request, *args, **kwargs)
        response_data = {'artistas': response_data.data}
        return JsonResponse(response_data)
class AlbumViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    def list(self, request, *args, **kwargs):
        response_data = super().list(request, *args, **kwargs)
        response_data = {'Albumes': response_data.data}
        return JsonResponse(response_data)
class CancionViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Cancion.objects.all()
    serializer_class = CancionSerializer
    def list(self, request, *args, **kwargs):
        response_data = super().list(request, *args, **kwargs)
        response_data = {'Canciones': response_data.data}
        return JsonResponse(response_data)
class GeneroViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    def list(self, request, *args, **kwargs):
        response_data = super().list(request, *args, **kwargs)
        response_data = {'Generos': response_data.data}
        return JsonResponse(response_data)


class ArtistaListView(ListView):
    model = Artista

class ArtistaDetailView(DetailView):
    model = Artista

class AlbumListView(ListView):
    model = Album

class AlbumDetailView(DetailView):
    model = Album

class CancionListView(ListView):
    model = Cancion

class CancionDetailView(DetailView):
    model = Cancion
    
class CancionUpdate(UpdateView):
    model = Cancion
    fields = [
'album',
'genero',
'titulo'] 

class CancionCreate(CreateView):
    model = Cancion
    fields = '__all__'

class CancionDelete(DeleteView):
    model = Cancion
    success_url = reverse_lazy('cancion-list')
    
class GeneroDetailView(DetailView):
    model = Genero
    template_name = 'genero_detail.html'  
    
class GeneroListView(ListView):
    model = Genero  
    template_name = 'genero_list.html'  
    context_object_name = 'genero'

class GeneroUpdate(UpdateView):
    model = Genero
    template_name = 'genero_form.html'  
    fields = '_all_'

class GeneroCreate(CreateView):
    model = Genero
    template_name = 'genero_form.html'  
    fields = '_all_'

class GeneroDelete(DeleteView):
    model = Genero
    template_name = 'genero_confirm_delete.html'  
    success_url = reverse_lazy('genero-list')

class AlbumUpdate(UpdateView):
    model = Album
    template_name = 'album_form.html'  
    fields = [
'artista',
'titulo',
'fecha',
'photo']

class AlbumCreate(CreateView):
    model = Album
    template_name = 'album_form.html'  
    fields = '_all_'

class AlbumDelete(DeleteView):
    model = Album
    template_name = 'album_confirm_delete.html'  
    success_url = reverse_lazy('Album-list')

class ArtistaUpdate(UpdateView):
    model = Artista
    template_name = 'artista_form.html'  
    fields = [
'nombre',
'edad',
'trayectoria',
'photo']
    

class ArtistaCreate(CreateView):
    model = Artista
    template_name = 'artista_form.html'  
    fields = '_all_'

class ArtistaDelete(DeleteView):
    model = Artista
    template_name = 'artista_confirm_delete.html'  
    success_url = reverse_lazy('artista-list')