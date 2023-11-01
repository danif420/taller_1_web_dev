from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse

class Artista(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    trayectoria = models.IntegerField()
    photo = models.ImageField(upload_to='artista/')
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Album(models.Model):
    artista = models.ForeignKey('Artista', on_delete=models.PROTECT,related_name='get_album' )
    titulo = models.CharField(max_length=50)
    fecha = models.DateField()
    photo = models.ImageField(upload_to='album/')
    
    def get_absolute_url(self):
        return reverse('album-list')
    
    def __str__(self):
        return self.titulo
    
class Cancion(models.Model):
    album = models.ForeignKey('Album', on_delete=models.PROTECT,related_name='get_cancion')
    genero = models.ForeignKey('Genero', on_delete=models.PROTECT,related_name='get_cancion')
    titulo = models.CharField(max_length=50)
    
    def get_absolute_url(self):
        return reverse('album-list')
    
    def __str__(self):
        return self.titulo
    
class Genero(models.Model):
    nombre = models.CharField(max_length=50)
    
    def get_absolute_url(self):
        return reverse('genero-list')
    
    def __str__(self):
        return self.nombre