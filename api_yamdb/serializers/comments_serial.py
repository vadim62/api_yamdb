from rest_framework import serializers

from api_yamdb.models import Comments


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Comments
