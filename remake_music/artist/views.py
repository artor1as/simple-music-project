from rest_framework import generics, permissions

from artist.models import Artist
from artist.serializers import ArtistCRUDSerializer


class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistCRUDSerializer
    permission_classes = (permissions.IsAdminUser,)


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistCRUDSerializer
    permission_classes = (permissions.IsAdminUser,)

