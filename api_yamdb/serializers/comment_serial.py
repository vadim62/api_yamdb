from rest_framework import serializers

from api_yamdb.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        read_only_fields = ('id', 'review', 'pub_date')
        fields = '__all__'
        model = Comment
