from rest_framework import generics, permissions

from album.models import Album
from album.serializers import AlbumCRUDSerializer


class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumCRUDSerializer
    permission_classes = (permissions.IsAdminUser,)


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumCRUDSerializer
    permission_classes = (permissions.IsAdminUser,)

