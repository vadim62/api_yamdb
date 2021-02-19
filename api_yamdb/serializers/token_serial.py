from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].required = False
        self.confirmation_code = kwargs.get('data').get('confirmation_code')

    def validate(self, attrs):
        attrs.update({'password': self.confirmation_code})
        return super().validate(attrs)
    