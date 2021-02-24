from rest_framework import filters, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)
from rest_framework.response import Response

from api_yamdb.models import Category
from api_yamdb.pagination import YamPagination
from api_yamdb.permissions.permissions import CategoriesGenresPermissions
from api_yamdb.serializers import CategoriesSerializer


class CategoriesViewSet(
    viewsets.GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    DestroyModelMixin
):
    pagination_class = YamPagination
    permission_classes = [CategoriesGenresPermissions]
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    filterset_fields = ['name', ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]

    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(Category, slug=self.kwargs['pk'])
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
