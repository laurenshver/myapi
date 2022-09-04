from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
# Create your views here.

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('release_year')
    serializer_class = AlbumSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('name')
    serializer_class = SongSerializer

class LyricViewSet(viewsets.ModelViewSet):
    queryset = Lyric.objects.all().order_by('song_id', 'order')
    serializer_class = LyricSerializer