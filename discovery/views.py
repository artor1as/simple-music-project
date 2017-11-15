from rest_framework import generics, permissions

from discovery.models import Discovery
from discovery.serializers import DiscoverCRUDSerializer


class DiscoveryList(generics.ListCreateAPIView):
    queryset = Discovery.objects.all()
    serializer_class = DiscoverCRUDSerializer
    permission_classes = (permissions.IsAdminUser,)


class DiscoveryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discovery.objects.all()
    serializer_class = DiscoverCRUDSerializer
    permission_classes = (permissions.IsAdminUser,)

