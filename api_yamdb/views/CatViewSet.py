
from rest_framework import filters, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, \
    ListModelMixin
from rest_framework.response import Response

from api_yamdb import serializers
from api_yamdb.models import Categories
from api_yamdb.pagination import YamPagination


class CategoriesViewSet(
    viewsets.GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    DestroyModelMixin
):
    pagination_class = YamPagination
    queryset = Categories.objects.all()
    serializer_class = serializers.CategoriesSerializer
    filterset_fields = ['name', ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]

    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(Categories, slug=self.kwargs['pk'])
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)