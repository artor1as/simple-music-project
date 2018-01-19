from rest_framework import serializers

from country.models import Country


class CountryCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
