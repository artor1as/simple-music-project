from django.contrib.auth.models import User
from rest_framework import serializers, validators

from remake_music.album.models import Album
from remake_music.artist.models import Artist
from remake_music.discovery.models import Discovery
from remake_music.like.models import Like
from remake_music.track.models import Track


class AlbumInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'name', 'year')


class TrackInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'name', 'artists', 'album', 'path')


class ArtistInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name')


class ArtistGeneralSerializer(ArtistInfoSerializer):
    albums = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = ('id', 'name', 'albums')

    def get_albums(self, obj):
        album_list = Album.objects.filter(artist=obj.id).values()
        return album_list


class AlbumGeneralSerializer(AlbumInfoSerializer):
    tracks = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ('id', 'name', 'year', 'tracks')

    def get_tracks(self, obj):
        track_list = Track.objects.filter(album=obj.id).values('id',
                                                               'name',
                                                               'path')
        return track_list


class DiscoveryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discovery
        fields = ('id', 'artist', 'order')


class LikeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'track', 'user')
        read_only_fields = ('user',)


class TrackGeneralSerializer(TrackInfoSerializer):
    album = AlbumInfoSerializer(read_only=True)
    artists = ArtistInfoSerializer(read_only=True, many=True)
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Track
        fields = ('id', 'name', 'artists', 'album', 'likes')

    def get_likes(self, obj):
        like_count = Track.objects.filter(id=obj.id).count()
        return like_count


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name',
                  'last_name', 'date_joined')
        read_only_fields = ('username', 'date_joined')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class PasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class SignupSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8, required=True)
    password_confirmation = serializers.CharField(min_length=8, required=True)
