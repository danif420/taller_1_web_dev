"""
URL configuration for musica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clasificacion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cancion/', views.CancionListView.as_view(), name='cancion-list'),
    path('cancion/<int:pk>/detail/', views.CancionDetailView.as_view(), name='cancion-detail'),
    path('genero/', views.GeneroListView.as_view(), name='genero-list'),
    path('genero/<int:pk>/detail/', views.GeneroDetailView.as_view(), name='genero-detail'),
    path('album/', views.AlbumListView.as_view(), name='album-list'),
    path('album/<int:pk>/detail/', views.AlbumDetailView.as_view(), name='album-detail'),
    path('artista/', views.ArtistaListView.as_view(), name='artista-list'),
    path('artista/<int:pk>/detail/', views.ArtistaDetailView.as_view(), name='artista-detail'),
    # Update
    path('cancion/<int:pk>/update/',views.CancionUpdate.as_view(),name='cancion-update'), 
    #Create
    path('cancion/create/', views.CancionCreate.as_view(), name='cancion-create'),
    #Delete
    path('cancion/<int:pk>/delete/', views.CancionDelete.as_view(), name='cancion-delete'),
]
