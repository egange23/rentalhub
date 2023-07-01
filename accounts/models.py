from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.db import models




class CustomUser(AbstractUser):
    phone = models.CharField(max_length=11, null=True, blank=True, unique=True, help_text="Enter mobile number")
    email_verification_code = models.CharField(max_length=50, null=True, blank=True,)
    email_verified = models.BooleanField(default=False, null=True, blank=True)
    phone_verification_code = models.CharField(max_length=50, null=True, blank=True,)
    phone_verified = models.BooleanField(default=False, null=True, blank=True)
    def __str__(self):
        return  self.username
 
 