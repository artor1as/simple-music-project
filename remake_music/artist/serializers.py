from rest_framework import serializers

from remake_music.artist.models import Artist


class ArtistCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
