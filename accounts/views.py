from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm
from .models import CustomUser




class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "accounts/registration/signup.html"
    success_url = reverse_lazy('login')
