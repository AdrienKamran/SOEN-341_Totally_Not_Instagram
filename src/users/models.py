from django.contrib.auth.models import AbstractUser

from django.db import models

#Inherited from abstract class for users
class CustomUser(AbstractUser):
    pass