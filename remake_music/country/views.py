from rest_framework import generics, permissions

from remake_music.country.models import Country
from remake_music.country.serializers import CountryCRUDSerializer


class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryCRUDSerializer
    permission_classes = (permissions.IsAdminUser,)


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryCRUDSerializer
    permission_classes = (permissions.IsAdminUser,)

