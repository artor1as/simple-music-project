from rest_framework import serializers

from remake_music.discovery.models import Discovery


class DiscoverCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discovery
        fields = '__all__'
