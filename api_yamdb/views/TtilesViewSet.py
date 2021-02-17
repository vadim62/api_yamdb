from rest_framework import viewsets

from api_yamdb import serializers
from api_yamdb.models import Titles
from api_yamdb.pagination import YamPagination


class TitlesViewSet(viewsets.ModelViewSet):
    pagination_class = YamPagination
    # permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    queryset = Titles.objects.all()
    serializer_class = serializers.TitlesSerializer
