from api_yamdb import serializers
from rest_framework_simplejwt.views import TokenViewBase


class MyTokenObtainPairView(TokenViewBase):
    serializer_class = serializers.MyTokenObtainPairSerializer