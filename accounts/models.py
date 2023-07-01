from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.db import models

import random, math

def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=11, null=True, blank=True, unique=True, help_text="Enter mobile number")
    verified = models.BooleanField(default=False, null=True, help_text="Complete User Verification")
    def __str__(self):
        return  self.username
 

    

