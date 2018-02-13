from rest_framework import generics, permissions

from remake_music.track.models import Track
from remake_music.api_client.serializers import TrackGeneralSerializer


class TrackAPIList(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackGeneralSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TrackAPIDetail(generics.RetrieveAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackGeneralSerializer
    permission_classes = (permissions.IsAuthenticated,)
