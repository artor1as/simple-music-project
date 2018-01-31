from rest_framework import serializers

from remake_music.album.models import Album
from remake_music.artist.models import Artist
from remake_music.discovery.models import Discovery
from remake_music.like.models import Like
from remake_music.track.models import Track


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
