from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.core.mail import send_mail
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm
from .models import CustomUser




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


def check_phone(request):
    phone = request.POST.get('phone')
    if get_user_model().objects.filter(phone=phone).exists():
        return HttpResponse("That phone number is already used")
    elif len(phone) == 10:
        return HttpResponse("That phone number is <strong style='color:green'> available! </strong>")
    elif len(phone) != 10:
        return HttpResponse("That phone number is <strong style='color:green'> too long or too short </strong>")

def check_email(request):
    email = request.POST.get('email')
    if get_user_model().objects.filter(email=email).exists():
        return HttpResponse("That email address is already in use. <a href='/accounts/password_reset'> Want to Login instead?</a>")
    else:
        return HttpResponse("That email address is <strong style='color:green'> available! </strong>")
