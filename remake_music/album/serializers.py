from rest_framework import serializers

from remake_music.album.models import Album


class AlbumCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
