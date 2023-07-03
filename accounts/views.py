from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.views.generic.edit import UpdateView
from django.core.mail import send_mail
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm, ContactVerificationForm
from .models import *
from django.conf import settings

import random, math

class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "accounts/registration/signup.html"
    success_url = reverse_lazy('login')

def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def get_email_code(request):
    customuser = CustomUser.objects.get(username=request.user)
    email_otp = generateOTP()
    customuser.email_verification_code = email_otp
    customuser.save()

    email = request.POST.get('email')
    subject = "Account Verification"
    message = f"Please verify your account with this code {email_otp}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,from_email,recipient_list)
    return HttpResponse("Email verification code sent!!")


    return redirect("verify")
    
def get_phone_code(*args):
    customuser = CustomUser.objects.get(username=args.user)
    phone_otp = generateOTP()
    customuser.phone_verification_code = phone_otp
    customuser.save()
    print(phone_otp)
    return redirect("verify")

class VerifyView(UpdateView):
    models = CustomUser
    form_class = ContactVerificationForm
    template_name = "accounts/registration/verification.html"
    success_url = reverse_lazy('verify')
    
    def get_object(self, queryset=CustomUser):
        print(self.request.user.verification_status)
        return self.request.user


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

def send_email_otp(request):
    print(refresh_email_code(request))
    


# How will verification be done?
# Each CustomUser has a verification_code variable that can be completed from a verification.html form.
# The verification.html has form that allows the user to enter their email address, email_verification_code, a button for verification <button>'s.
