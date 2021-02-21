from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UsersSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='Пользователь с таким email уже существует!'
            ),
        ]
    )
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='Пользователь с таким username уже существует!'
            ),
        ]
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'bio', 'email', 'role'
        )
