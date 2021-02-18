from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated 

from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework.viewsets import ModelViewSet

from api_yamdb import settings
from .permissions import UsersPermissions
from .serializers import (
    MyTokenObtainPairSerializer, UsersSerializer, RegisterSerializer
)


User = get_user_model()
 

class MyTokenObtainPairView(TokenViewBase):
    serializer_class = MyTokenObtainPairSerializer


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


class RegisterUserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def send_confirmation_code(self, email, token):
        subject = 'Confirmation code'
        message = f'Confirmation code: {token}'
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, [email,])

    def perform_create(self, serializer):
        email = serializer.validated_data['email']
        # создаем пользователя без пароля
        user = User.objects.create(email=email)
        # создаем confirmation_code, он же - пароль для пользователя
        confirmation_code = default_token_generator.make_token(user)
        # устанавливаем хэш-пароль для пользователя
        user.set_password(confirmation_code)
        # сохраняем пароль пользователя
        user.save()
        # отправляем confirmation_code на почту пользователя
        self.send_confirmation_code(email, confirmation_code)
        