from api_yamdb import serializers
from api_yamdb.models import Review
from api_yamdb.pagination import YamPagination
from api_yamdb.permissions.permissions import CommentPermissions

from django.shortcuts import get_object_or_404

from rest_framework import viewsets


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    pagination_class = YamPagination
    permission_classes = [CommentPermissions]

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return review.comments.all().order_by('id')

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)
