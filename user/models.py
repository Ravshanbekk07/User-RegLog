from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Custom User model
    """
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.username