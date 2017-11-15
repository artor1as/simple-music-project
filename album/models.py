from datetime import date, datetime
from django.db import models

from artist.models import Artist

YEAR_CHOICES = [(r, r) for r in range(1960, date.today().year+1)]


class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist)
    year = models.IntegerField('year',
                               choices=YEAR_CHOICES,
                               default=datetime.now().year)

    def __str__(self):
        return '{0}, {1}'.format(self.name, self.year)

    class Meta:
        db_table = 'album'
