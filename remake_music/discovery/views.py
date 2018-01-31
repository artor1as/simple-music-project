from rest_framework import generics, permissions

from remake_music.discovery.models import Discovery
from remake_music.discovery.serializers import DiscoverCRUDSerializer


class DiscoveryList(generics.ListCreateAPIView):
    queryset = Discovery.objects.all()
    serializer_class = DiscoverCRUDSerializer
    permission_classes = (permissions.IsAdminUser,)


class DiscoveryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discovery.objects.all()
    serializer_class = DiscoverCRUDSerializer
    permission_classes = (permissions.IsAdminUser,)

