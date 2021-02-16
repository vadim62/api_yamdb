from rest_framework import viewsets

from api_yamdb import serializers
from api_yamdb.models import Categories


class CategoriesViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    queryset = Categories.objects.all()
    serializer_class = serializers.CategoriesSerializer



