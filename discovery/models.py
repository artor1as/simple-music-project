from django.db import models

from artist.models import Artist


class Discovery(models.Model):
    artist = models.ForeignKey(Artist)
    order = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return '{0} - {1}'.format(self.artist, self.order)

    class Meta:
        ordering = ['order']
