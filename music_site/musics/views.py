from django.shortcuts import render

# Create your views here.
from django.views import generic
from . import models
# Create your models here.


class Home(generic.ListView):
    template_name='musics/home.html'
    context_object_name = 'musician_list'

    def get_queryset(self):
        return models.Musician.objects.all()

class MusicianDetail(generic.DetailView):
    model = models.Musician
    template_name='musics/musician_detail.html'

class AlbumDetail(generic.DetailView):
    model = models.Album
    template_name='musics/album_detail.html'

class SongDetail(generic.DetailView):
    model = models.Song
    template_name='musics/song_detail.html'
    