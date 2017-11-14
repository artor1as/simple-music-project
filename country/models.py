from django.db import models


class Country(models.Model):
    id = models.CharField(max_length=2, primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return '{0}, {1}'.format(self.id, self.name)

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Countries'
