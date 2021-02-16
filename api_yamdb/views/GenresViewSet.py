from rest_framework import viewsets

from api_yamdb import serializers
from api_yamdb.models import Genres


class GenresViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    queryset = Genres.objects.all()
    serializer_class = serializers.GenresSerializer



