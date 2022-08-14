from django.db import models

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=50)
    release_year = models.SmallIntegerField()

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=100)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Lyric(models.Model):
    lyric = models.CharField(max_length=100)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    order = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.lyric