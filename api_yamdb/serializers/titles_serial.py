from rest_framework import serializers

from api_yamdb.models import Genres, Titles


class TitlesSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        many=True,
        slug_field='slug',
        queryset=Genres.objects.all(),
        required=False,
    ),

    class Meta:
        exclude = ['id', ]
        model = Titles
