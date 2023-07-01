from django.urls import path
from .views import SignUpView, VerifyView
from . import views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("verify/", VerifyView.as_view(), name="verify"),

]

htmx_urlpatterns = [
    path("check_username/", views.check_username, name='check-username'),
    path("check_phone/", views.check_phone, name='check-phone'),
    path("check_email/", views.check_email, name='check-email'),
    path("verify_email/", views.send_verification_code, name='verify-email'),
]

urlpatterns += htmx_urlpatterns

