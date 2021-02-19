from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticated 
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from api_yamdb import settings
from api_yamdb.serializers import UsersSerializer
from api_yamdb.permissions.permissions import UsersPermissions


User = get_user_model()
 

class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
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
