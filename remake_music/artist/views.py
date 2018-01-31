from rest_framework import generics, permissions

from remake_music.artist.models import Artist
from remake_music.artist.serializers import ArtistCRUDSerializer


class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistCRUDSerializer
    permission_classes = (permissions.IsAdminUser,)


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistCRUDSerializer
    permission_classes = (permissions.IsAdminUser,)

