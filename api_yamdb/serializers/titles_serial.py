from rest_framework import serializers

from api_yamdb.models import Genres, Titles


class TitlesSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        many=True,
        queryset=Genres.objects.all(),
        slug_field='slug',
        required=False,
    ),
    # genre = serializers.StringRelatedField(many=True)

    class Meta:
        fields = '__all__'
        model = Titles
