from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Add any additional fields you want to include in your custom user model
    # For example:
    # bio = models.TextField(blank=True)
    pass
# Create your models here.
