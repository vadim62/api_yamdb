from rest_framework import serializers

from api_yamdb.models import Categories, Genres, Titles
from . import CategoriesSerializer
from . import GenresSerializer


class TitlesSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genres.objects.all(),
        slug_field='slug',
        required=False,
        many=True,
    ),
    id = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    category = serializers.SlugRelatedField(
        queryset=Categories.objects.all(),
        slug_field='slug',
        required=False,
    )

    class Meta:
        fields = '__all__'
        model = Titles


class TitleReadSerializer(serializers.ModelSerializer):
    genre = GenresSerializer(many=True)
    category = CategoriesSerializer(required=False)

    class Meta:
        fields = '__all__'
        model = Titles
