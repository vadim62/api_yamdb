from api_yamdb import settings
from api_yamdb.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

User = get_user_model()


class RegisterUserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def send_confirmation_code(self, email, token):
        subject = 'Confirmation code'
        message = f'Confirmation code: {token}'
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, [email, ])

    def perform_create(self, serializer):
        email = serializer.validated_data.get('email')          
        # создаем пользователя без пароля
        user, created = User.objects.get_or_create(email=email)
        # создаем confirmation_code, он же - пароль для пользователя
        confirmation_code = default_token_generator.make_token(user)
        # устанавливаем хэш-пароль для пользователя
        user.set_password(confirmation_code)
        # сохраняем пароль пользователя
        user.save()
        # отправляем confirmation_code на почту пользователя
        self.send_confirmation_code(email, confirmation_code)
