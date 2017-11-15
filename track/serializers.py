from rest_framework import serializers

from track.models import Track


class TrackCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'
