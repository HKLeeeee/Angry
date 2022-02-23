from django.db import models
from django.contrib.auth.models import AbstractUser


class Member(AbstractUser):
    mobile = models.CharField(max_length=20)
