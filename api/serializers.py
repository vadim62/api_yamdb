from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].required = False
        self.confirmation_code = kwargs.get('data').get('confirmation_code')
    
    def validate(self, attrs):
        attrs.update({'password': self.confirmation_code})
        return super().validate(attrs)
   

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'bio', 'email', 'role'
        )


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
  