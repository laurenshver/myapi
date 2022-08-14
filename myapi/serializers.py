from dataclasses import field
from rest_framework import serializers
from .models import *

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ('name', 'release_year')