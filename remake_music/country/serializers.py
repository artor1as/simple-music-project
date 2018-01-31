from rest_framework import serializers

from remake_music.country.models import Country


class CountryCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
