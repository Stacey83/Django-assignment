from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

class CreateAccountView(models.Model):
    username = models.CharField
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.username
