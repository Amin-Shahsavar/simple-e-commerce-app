from django.db import models
from django.contrib.auth.models import User, AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
