from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from api_yamdb import serializers
from api_yamdb.models import Review
from api_yamdb.pagination import YamPagination
from api_yamdb.permissions.permissions import CommentPermissions


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    pagination_class = YamPagination
    permission_classes = [CommentPermissions]

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return review.comments.all().order_by('id')

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, pk=review_id, title__id=title_id)
        serializer.save(author=self.request.user, review=review)
