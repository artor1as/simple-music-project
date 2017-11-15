from django.db import models

from country.models import Country
from artist.models import Artist
from album.models import Album


class Track(models.Model):
    name = models.CharField(max_length=100)
    artists = models.ManyToManyField(Artist)
    album = models.ForeignKey(Album)
    path = models.CharField(max_length=100, default='/home/music')
    available_country = models.ManyToManyField(
        Country,
        default=Country.objects.all(),
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'track'
