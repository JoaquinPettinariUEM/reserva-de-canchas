from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_club_owner = models.BooleanField(default=False)
    name = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    country = models.CharField(max_length=50, blank=True)
    document = models.CharField(max_length=50, unique=True, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
