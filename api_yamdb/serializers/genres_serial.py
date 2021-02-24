from rest_framework import serializers

from api_yamdb.models import Genre


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Genre
