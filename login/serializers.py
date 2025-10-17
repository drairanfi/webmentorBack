from rest_framework import serializers  
from django.contrib.auth import get_user_model 
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

# Serializador para el modelo de usuario personalizado
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


# Serializador para el registro de usuarios
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user