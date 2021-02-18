from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from api_yamdb import serializers
from api_yamdb.models import Review


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentsSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self, review_id=None):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        return review.comments
