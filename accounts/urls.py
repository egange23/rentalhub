from django.urls import path
from .views import SignUpView, EmailVerifyView, PhoneVerifyView
from . import views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("verify_email/", EmailVerifyView.as_view(), name="verify_email"),
    path("verify_phone/", PhoneVerifyView.as_view(), name="verify_phone"),
    path("send_email_code/", views.send_email_code, name="send_email_code"),
    path("send_phone_code/", views.send_phone_code, name="send_phone_code"),

]

htmx_urlpatterns = [
    path("check_username/", views.check_username, name='check-username'),
    path("check_phone/", views.check_phone, name='check-phone'),
    path("check_email/", views.check_email, name='check-email'),
]

urlpatterns += htmx_urlpatterns

