from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework import generics

User = get_user_model()

# Clase para registrar los usuarios
class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        """
        Registra un nuevo usuario y devuelve los tokens JWT.
        """
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # Generar tokens JWT para el usuario recién registrado
            refresh = RefreshToken.for_user(user)
            
            return Response({
                'message': 'Usuario registrado exitosamente',
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                },
                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Clase para listar todos los usuarios
class UserListView(APIView):
    permission_classes = [IsAuthenticated]  # Requiere autenticación
    
    def get(self, request):
        """
        Lista todos los usuarios registrados.
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        
        return Response({
            'count': users.count(),
            'users': serializer.data
        }, status=status.HTTP_200_OK)


# Clase para obtener detalles de un usuario específico
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, user_id):
        """
        Obtiene los detalles de un usuario específico.
        """
        try:
            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({
                'error': 'Usuario no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)