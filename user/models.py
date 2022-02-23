from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Member(AbstractUser):
        phone_number = models.CharField(max_length=20)
