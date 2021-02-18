from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS

from api_yamdb import serializers
from api_yamdb.filters import TitlesFilter
from api_yamdb.models import Titles
from api_yamdb.pagination import YamPagination


class TitlesViewSet(viewsets.ModelViewSet):
    pagination_class = YamPagination
    queryset = Titles.objects.all()
    serializer_class = serializers.TitlesSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TitlesFilter

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializers.TitleReadSerializer
        return serializers.TitlesSerializer



