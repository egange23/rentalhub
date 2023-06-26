from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=11, null=True, blank=True, unique=True, help_text="Enter mobile number")
    email = models.EmailField(unique=True, null=True, help_text="...")
    def __str__(self):
        return  self.username
 

    
    