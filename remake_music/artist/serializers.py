from rest_framework import serializers

from artist.models import Artist


class ArtistCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
