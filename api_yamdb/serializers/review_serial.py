from rest_framework import serializers

from api_yamdb.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Review
