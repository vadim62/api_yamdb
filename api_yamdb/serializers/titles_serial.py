from rest_framework import serializers

from api_yamdb.models import Categories, Genres, Titles


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ['slug']


class TitlesSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)

    class Meta:
        exclude = ['id', ]
        model = Titles