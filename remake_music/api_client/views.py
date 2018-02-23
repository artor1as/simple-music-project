from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets

from remake_music.album.models import Album
from remake_music.api_client.permissions import (OnlyUserCanOrReadOnly,
                                                 OnlyAnonUserCan)
from remake_music.artist.models import Artist
from remake_music.track.models import Track
from remake_music.like.models import Like
from remake_music.api_client.serializers import (TrackGeneralSerializer,
                                                 LikeInfoSerializer,
                                                 UserSerializer,
                                                 ArtistGeneralSerializer,
                                                 AlbumGeneralSerializer)


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackGeneralSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.prefetch_related('album_set').all()
    serializer_class = ArtistGeneralSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().select_related('artist')
    serializer_class = AlbumGeneralSerializer
    permission_classes = (permissions.IsAuthenticated,)


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeInfoSerializer
    permission_classes = (permissions.IsAuthenticated, OnlyUserCanOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class UserAPISignup(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (OnlyAnonUserCan,)


class UserAPIUpdateDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (OnlyUserCanOrReadOnly,)
