from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.validators import UniqueValidator


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='Такой пользователь уже существует!'
            ),
        ]
    )

    class Meta:
        model = User
        fields = (
            'email',
        )
