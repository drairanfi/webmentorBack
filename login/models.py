from django.db import models
from django.contrib.auth.models import AbstractUser

# Se van a crear los modelos para registrar los usuarios con email 

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
