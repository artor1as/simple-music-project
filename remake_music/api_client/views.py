from django.contrib.auth.models import User
from rest_framework import generics, permissions

from remake_music.api_client.permissions import OnlyUserCanOrReadOnly
from remake_music.track.models import Track
from remake_music.like.models import Like
from remake_music.api_client.serializers import (TrackGeneralSerializer,
                                                 LikeInfoSerializer,
                                                 UserSerializer, )


class TrackAPIList(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackGeneralSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TrackAPIDetail(generics.RetrieveAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackGeneralSerializer
    permission_classes = (permissions.IsAuthenticated,)


class LikeAPIList(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeInfoSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeAPIDetail(generics.RetrieveUpdateDestroyAPIView):
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
    permission_classes = (permissions.AllowAny,)


class UserAPIUpdateDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (OnlyUserCanOrReadOnly,)
