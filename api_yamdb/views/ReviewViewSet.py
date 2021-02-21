from api_yamdb.models import Title
from api_yamdb.pagination import YamPagination
from api_yamdb.permissions.permissions import ReviewPermissions
from api_yamdb.serializers.review_serial import ReviewSerializer
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = YamPagination
    permission_classes = [ReviewPermissions]

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all().order_by('id')

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)
