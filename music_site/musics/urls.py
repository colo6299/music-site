from django.urls import path
from . import views

urlpatterns = [

    path('', views.Home.as_view(), name='home'),
    path('musician/<int:pk>/', views.MusicianDetail.as_view(), name='musician detail'),
    path('album/<int:pk>/', views.AlbumDetail.as_view(), name='album detail'),
    path('song/<int:pk>/', views.SongDetail.as_view(), name='song detail')

]