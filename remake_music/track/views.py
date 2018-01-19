from rest_framework import generics, permissions

from track.models import Track
from track.serializers import TrackCRUDSerializer


class TrackList(generics.ListCreateAPIView):
    queryset = Track.objects.prefetch_related(
        'available_country').prefetch_related('artists')
    serializer_class = TrackCRUDSerializer
    permission_classes = (permissions.IsAdminUser,)


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackCRUDSerializer
    permission_classes = (permissions.IsAdminUser,)

