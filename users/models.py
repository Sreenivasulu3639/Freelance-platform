from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Freelancer'),
        (2, 'Client'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
from django.db import models

# Create your models here.
