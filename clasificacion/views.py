from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from clasificacion.models import Artista,Album,Cancion,Genero
from django.urls import reverse_lazy

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
    fields = '__all__' 

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
    success_url = reverse_lazy('genero_list')

class AlbumUpdate(UpdateView):
    model = Album
    template_name = 'album_form.html'  
    fields = '_all_',

class AlbumCreate(CreateView):
    model = Album
    template_name = 'album_form.html'  
    fields = '_all_'

class AlbumDelete(DeleteView):
    model = Album
    template_name = 'album_confirm_delete.html'  
    success_url = reverse_lazy('Album_list')