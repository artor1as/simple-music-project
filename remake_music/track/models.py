from django.db import models

from remake_music.country.models import Country
from remake_music.artist.models import Artist
from remake_music.album.models import Album


class Track(models.Model):
    name = models.CharField(max_length=100)
    artists = models.ManyToManyField(Artist)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    path = models.CharField(max_length=100, default='/home/music')
    available_country = models.ManyToManyField(Country)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'track'
