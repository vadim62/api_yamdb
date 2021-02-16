from rest_framework import serializers

from api_yamdb.models import Categories, Genres, Titles


class TitlesSerializer(serializers.ModelSerializer):
    # category = serializers.SlugRelatedField(many=True, queryset=Categories.objects, slug_field='id')

    class Meta:
        exclude = ['id', ]
        model = Titles
