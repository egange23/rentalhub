from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from accounts.models import CustomUser


# Create your views here.

class HomePageView(ListView):
    model = CustomUser
    template_name = "pages/home.html"


