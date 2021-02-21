from api_yamdb import serializers
from api_yamdb.filters import TitlesFilter
from api_yamdb.models import Title
from api_yamdb.pagination import YamPagination
from api_yamdb.permissions.permissions import TitlesPermissions

from django.db.models import Avg

from django_filters import rest_framework as filters

from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')
    ).order_by('id')
    permission_classes = [TitlesPermissions]
    pagination_class = YamPagination
    serializer_class = serializers.TitlesSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TitlesFilter

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializers.TitleReadSerializer
        return serializers.TitlesSerializer
