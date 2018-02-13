from rest_framework import generics, permissions

from remake_music.album.models import Album
from remake_music.album.serializers import AlbumCRUDSerializer


class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumCRUDSerializer
    permission_classes = (permissions.IsAdminUser,)


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumCRUDSerializer
    permission_classes = (permissions.IsAdminUser,)
