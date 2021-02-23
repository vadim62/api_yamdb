from rest_framework import serializers

from api_yamdb.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    permission_classes = []
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        read_only_fields = ('id', 'title', 'pub_date')
        fields = '__all__'
        model = Review

    def validate(self, attrs):
        exist = Review.objects.filter(
            author=self.context['request'].user,
            title=self.context['view'].kwargs.get('title_id')).exists()
        if exist and self.context['request'].method == 'POST':
            raise serializers.ValidationError(
                'Пользователь уже оставлял отзыв на это произведение')
        return attrs
