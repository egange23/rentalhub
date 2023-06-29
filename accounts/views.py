from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.core.mail import send_mail
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm
from .models import CustomUser
from django.conf import settings

import random, math



class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "accounts/registration/signup.html"
    
    success_url = reverse_lazy('login')

def check_username(request):
    username = request.POST.get('username')
    username_length = len(username)
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("That <b>username</b> already exists. <a href='/accounts/password_reset'> Want to Login instead?</a> ")
    elif username_length > 5:
        return HttpResponse("That username is <strong style='color:green'> available! </strong>")
    else:
        return HttpResponse('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')


def check_phone(request):
    phone = request.POST.get('phone')
    if get_user_model().objects.filter(phone=phone).exists():
        return HttpResponse("That phone number is already used")
    elif len(phone) >= 10 and phone.isnumeric():
        return HttpResponse("That phone number is <strong style='color:green'> available! </strong>")
    else:
        return HttpResponse("Enter mobile number")

def check_email(request):
    email = request.POST.get('email')
    if get_user_model().objects.filter(email=email).exists():
        return HttpResponse("That email address is already in use. <a href='/accounts/password_reset'> Want to Login instead?</a>")
    elif '@' in email and len(email) >=10:
        return HttpResponse("That email address is <strong style='color:green'> available! </strong>")
    else:
        return HttpResponse("...")

def generateOTP():
    digits = "0123456789"
    OTP = ""

    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP



def verify_email(request):
    verification_code = generateOTP()
    email = request.POST.get('email')
    subject = "Account Verification"
    message = f"Please verify your account {verification_code}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,from_email,recipient_list)
    print(email)
    
    return HttpResponse("Verification code sent!")