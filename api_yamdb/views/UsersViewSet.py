from api_yamdb.permissions.permissions import UsersPermissions
from api_yamdb.serializers import UsersSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

User = get_user_model()


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (
        IsAuthenticated,
        UsersPermissions,
    )
    pagination_class = PageNumberPagination

    def get_object(self):
        username = self.kwargs['pk']
        if username == 'me':
            user = self.request.user
        else:
            user = get_object_or_404(User, username=username)
        self.kwargs['pk'] = user.pk
        return super().get_object()
