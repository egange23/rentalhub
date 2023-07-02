from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUser

class TextInput(forms.TextInput):
    input_type: 'str'

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields
        widgets = {
            "username": forms.TextInput(attrs={'hx-post': '/accounts/check_username/', 'hx-trigger':'keyup changed delay:1000ms', 'hx-target':'#hint_id_username',}),
                   }          
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

        widgets = {
             "phone": forms.TextInput(attrs={'hx-post': '/accounts/check_phone/', 'hx-trigger':'keyup changed delay:1000ms', 'hx-target':'#hint_id_phone',}),
             "email": forms.TextInput(attrs={'hx-post':'/accounts/check_email/', 'hx-trigger':'keyup changed delay:1000ms', 'hx-target':'#hint_id_email',}),
                   }   

class ContactVerificationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("email","enter_email_verification_code","phone", "enter_phone_verification_code",)

        widgets = {
             "phone": forms.TextInput(attrs={'hx-post': '/accounts/check_phone/', 'hx-trigger':'keyup changed delay:1000ms', 'hx-target':'#hint_id_phone',}),
             "email": forms.TextInput(attrs={'hx-post':'/accounts/check_email/', 'hx-trigger':'keyup changed delay:1000ms', 'hx-target':'#hint_id_email',}),
             "enter_email_verification_code": forms.TextInput(attrs={'hx-post':'/accounts/check_email/', 'hx-trigger':'keyup changed delay:1000ms', 'hx-target':'#hint_id_email' ,})
                   }
