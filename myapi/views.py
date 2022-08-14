from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
# Create your views here.

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('release_year')
    serializer_class = AlbumSerializer