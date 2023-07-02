from django.urls import path
from .views import SignUpView, VerifyView
from . import views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("verify/", VerifyView.as_view(), name="verify"),
    path("refresh_email_code/", views.refresh_email_code, name="refresh_email_code"),
     path("refresh_phone_code/", views.refresh_phone_code, name="refresh_phone_code"),

]

htmx_urlpatterns = [
    path("check_username/", views.check_username, name='check-username'),
    path("check_phone/", views.check_phone, name='check-phone'),
    path("check_email/", views.check_email, name='check-email'),
    path("send_email_otp/", views.send_email_otp, name='send-email-otp'),

    
]

urlpatterns += htmx_urlpatterns

