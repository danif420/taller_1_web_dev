from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.
class Artista(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    trayectoria = models.IntegerField()
    photo = models.ImageField(upload_to='artista/')
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Album(models.Model):
    x1 = models.ForeignKey('Selection', on_delete=models.PROTECT,related_name='get_players' )
    titulo = models.CharField(max_length=50)
    fecha = models.DateField(max_length=50)
    photo = models.ImageField(upload_to='album/')
    def get_absolute_url(self):
        return reverse('album-list')
    
    def __str__(self):
        return self.titulo
    
class Cancion(models.Model):
    titulo = models.ForeignKey('Selection', on_delete=models.PROTECT,related_name='get_players' )
    fecha = models.DateField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='album/')
    def get_absolute_url(self):
        return reverse('album-list')
    
    def __str__(self):
        return self.titulo