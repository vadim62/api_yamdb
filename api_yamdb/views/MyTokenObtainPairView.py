from rest_framework_simplejwt.views import TokenViewBase

from api_yamdb import serializers


class MyTokenObtainPairView(TokenViewBase):
    serializer_class = serializers.MyTokenObtainPairSerializer
