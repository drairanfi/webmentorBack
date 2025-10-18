from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)
from .views import RegisterView, UserListView, UserDetailView, UserDeleteView

urlpatterns = [
    # endpoint para registrar nuevos usuarios
    path('register/', RegisterView.as_view(), name='register'),
    # endpoint para iniciar sesion y obtener tokens JWT
    # Este token se usara para iniciar sesion es decir en el js es donde se va a tener
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # endpoint para refrescar el token de acceso
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # endpoint para cerrar sesion y invalidar el token de refresco
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    # endpoint para listar todos los usuarios
    path('users/', UserListView.as_view(), name='user_list'),
    # endpoint para obtener detalles de un usuario específico
    path('users/<int:user_id>/', UserDetailView.as_view(), name='user_detail'),
    # endpoint para eliminar un usuario específico
    path('users/<int:user_id>/delete/', UserDeleteView.as_view(), name='user_delete'),

]