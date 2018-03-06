from django.contrib.auth.models import User
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from remake_music.album.models import Album
from remake_music.base import permissions as base_permissions
from remake_music.base import viewsets as base_viewsets
from remake_music.artist.models import Artist
from remake_music.track.models import Track
from remake_music.like.models import Like
from remake_music.api_client.serializers import (TrackGeneralSerializer,
                                                 LikeInfoSerializer,
                                                 UserSerializer,
                                                 ArtistGeneralSerializer,
                                                 AlbumGeneralSerializer,
                                                 PasswordSerializer,
                                                 SignupSerializer)


class TrackViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackGeneralSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ArtistViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Artist.objects.prefetch_related('album_set').all()
    serializer_class = ArtistGeneralSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AlbumViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Album.objects.all().select_related('artist')
    serializer_class = AlbumGeneralSerializer
    permission_classes = (permissions.IsAuthenticated,)


class LikeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeInfoSerializer
    permission_classes = (permissions.IsAuthenticated,
                          base_permissions.OnlyUserCanOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class UserSignupViewSet(base_viewsets.CreateViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (base_permissions.OnlyAnonUserCan,)

    @list_route(methods=['post'], serializer_class=SignupSerializer)
    def signup(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(base_viewsets.ReadUpdateViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (base_permissions.OnlyUserCanOrReadOnly,)

    @detail_route(methods=['put'], serializer_class=PasswordSerializer)
    def change_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            if not user.check_password(serializer.data.get('old_password')):
                return Response({'old_password': ['Wrong password!']},
                                status=status.HTTP_400_BAD_REQUEST)
            if not len(serializer.data.get('new_password')) >= 8:
                return Response({'new_password': [
                    'Password must have at least 8 characters.']},
                    status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.data.get('new_password'))
            user.save()
            return Response({'status': 'Password changed successfully!'})
