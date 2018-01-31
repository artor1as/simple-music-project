from rest_framework import generics, permissions

from remake_music.like.models import Like
from remake_music.like.serializers import LikeCRUDSerializer


class LikeList(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeCRUDSerializer
    permission_classes = (permissions.IsAdminUser,)


class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeCRUDSerializer
    permission_classes = (permissions.IsAdminUser,)

