from django.contrib.auth.models import User
from django.db import models

from track.models import Track


class Like(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} - {1}'.format(self.track, self.user)

    class Meta:
        unique_together = ('user', 'track')
        verbose_name_plural = 'Likes'
        db_table = 'like'
