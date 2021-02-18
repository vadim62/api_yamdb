from rest_framework import serializers

from api_yamdb.models import Genres


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Genres
        