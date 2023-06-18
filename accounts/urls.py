from django.urls import path
from .views import SignUpView, SignUpGroupView
from . import views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("signup_group/", SignUpGroupView.as_view(), name="signup_group"),
    # path("profile", views.user_profile_view,name="profile"),
]