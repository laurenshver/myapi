from dataclasses import field
from rest_framework import serializers
from .models import *

class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ['order', 'lyric', 'song_id']
        depth = 2
        

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = [ 'id', 'name','album_id']
        depth = 1
        
class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    # songs = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    class Meta:
        model = Album
        fields = ('id', 'name', 'release_year')