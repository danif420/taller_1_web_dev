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
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from api import views as api_views
from clasificacion import views

router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'groups', api_views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('clasificacion.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
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
    # Update
    path('album/<int:pk>/update/',views.AlbumUpdate.as_view(),name='album-update'), 
    #Create
    path('album/create/', views.AlbumCreate.as_view(), name='album-create'),
    #Delete
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),
    # Update
    path('genero/<int:pk>/update/',views.GeneroUpdate.as_view(),name='genero-update'), 
    #Create
    path('genero/create/', views.GeneroCreate.as_view(), name='genero-create'),
    #Delete
    path('genero/<int:pk>/delete/', views.GeneroDelete.as_view(), name='genero-delete'),
    # Update
    path('artista/<int:pk>/update/',views.ArtistaUpdate.as_view(),name='artista-update'), 
    #Create
    path('artista/create/', views.ArtistaCreate.as_view(), name='artista-create'),
    #Delete
    path('artista/<int:pk>/delete/', views.ArtistaDelete.as_view(), name='artista-delete'),
]
urlpatterns += router.urls