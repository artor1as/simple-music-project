from django.db import models

from remake_music.artist.models import Artist


class Discovery(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return '{0} - {1}'.format(self.artist, self.order)

    class Meta:
        ordering = ['order']
        db_table = 'discovery'
        verbose_name_plural = 'Discoveries'
