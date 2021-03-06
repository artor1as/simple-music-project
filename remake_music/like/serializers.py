from rest_framework import serializers

from remake_music.like.models import Like


class LikeCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
