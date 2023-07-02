from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.db import models




class CustomUser(AbstractUser):
    email_verification_code = models.CharField(max_length=50, null=True, blank=True,)
    phone = models.CharField(max_length=11, null=True, blank=True, unique=True, help_text="Enter mobile number")
    enter_email_verification_code = models.CharField(max_length=50, null=True, blank=True,)
    email_verified = models.BooleanField(default=False, null=True, blank=True)
    phone_verification_code = models.CharField(max_length=50, null=True, blank=True,)
    enter_phone_verification_code = models.CharField(max_length=50, null=True, blank=True,)
    phone_verified = models.BooleanField(default=False, null=True, blank=True)
    def __str__(self):
        return  self.username
    
    def save(self, *args, **kwargs):
        self.email_verified = self.email_verification_code == self.enter_email_verification_code
        self.phone_verified = self.phone_verification_code == self.enter_phone_verification_code
        super().save(*args, **kwargs)
        

    @property
    def verification_status(self):
        if self.email_verified and self.phone_verified:
            return True
        else:
            return False