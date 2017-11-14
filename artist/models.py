from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=150)
    bio = models.TextField(max_length=5000)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'artist'
