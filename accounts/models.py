from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    email=models.EmailField()
    name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=20, unique=True)
    about=models.TextField(max_length=100, null=True, blank=True)
    username=models.CharField(max_length=50, unique=False, null=True, blank=True)
    
    USERNAME_FIELD='phone_number'
    REQUIRED_FIELD=["username","email", "name"]

    objects=CustomUserManager()

    def __str__(self):
        return self.name
