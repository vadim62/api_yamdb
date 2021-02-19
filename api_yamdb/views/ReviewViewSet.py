from rest_framework import viewsets

from api_yamdb import serializers
from api_yamdb.models import Review
from django.shortcuts import get_object_or_404


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self, review_id=None):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        return review.comments
