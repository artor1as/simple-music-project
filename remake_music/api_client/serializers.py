from rest_framework import serializers

from album.models import Album
from artist.models import Artist
from discovery.models import Discovery
from like.models import Like
from track.models import Track


class AlbumInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'name')


class TrackInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'name', 'artists', 'album', 'path')


class ArtistInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name')


class DiscoveryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discovery
        fields = ('id', 'artist', 'order')


class LikeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'track', 'user')
