from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'customer'),
        (2, 'seller'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
