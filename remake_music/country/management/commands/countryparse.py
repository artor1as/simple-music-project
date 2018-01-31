import requests
from django.core.management.base import BaseCommand

from remake_music.country.models import Country


class Command(BaseCommand):
    help = 'Parse country names with their codes in country table.'

    def handle(self, *args, **options):
        url = ('https://pkgstore.datahub.io/core/'
               'country-list:data_json/data/data_json.json')
        r = requests.get(url)
        json = r.json()
        for country in json:
            Country.objects.update_or_create(
                id=country['Code'],
                defaults=dict(name=country['Name'])
            )
        r.close()
