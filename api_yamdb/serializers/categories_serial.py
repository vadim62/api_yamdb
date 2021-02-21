from rest_framework import serializers

from api_yamdb.models import Category


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category
