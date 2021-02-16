from rest_framework import serializers

from api_yamdb.models import Categories


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        exclude = ('id',)
