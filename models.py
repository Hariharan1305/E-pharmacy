from django.db import models

# Create your models here.
# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    mobile_no=models.CharField(max_length=10)
    address=models.CharField(max_length=100)

    def __str__(self):
        return self.email