from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from clasificacion.models import Artista,Album,Cancion,Genero

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