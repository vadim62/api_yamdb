from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from api_yamdb.permissions import UsersPermissions
from api_yamdb import serializers


User = get_user_model()


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UsersSerializer
    permission_classes = (
        IsAuthenticated,
        UsersPermissions,
   )
    pagination_class = PageNumberPagination
    # filter_backends = (DjangoFilterBackend,)
    # filterset_class = UsersFilter


    def get_object(self):
        username = self.kwargs['pk']
        if username == 'me':
            user = self.request.user
        else:
            user = get_object_or_404(User, username=username)
        self.kwargs['pk'] = user.pk
        return super().get_object()
