from rest_framework import viewsets

from api_yamdb import serializers
from api_yamdb.models import Titles


class TitlesViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    queryset = Titles.objects.all()
    serializer_class = serializers.TitlesSerializer
