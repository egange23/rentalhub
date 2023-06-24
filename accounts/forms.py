from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUser

class TextInput(forms.TextInput):
    input_type: 'str'




class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("phone","email")
        widgets = {
            "username": forms.TextInput(attrs={'hx-post': '/accounts/check_username/', 'hx-trigger':'keyup', 'hx-target':'#div_error_message',}),
             "phone": forms.NumberInput(attrs={'hx-post': '/accounts/check_phone/', 'hx-trigger':'keyup', 'hx-target':'#div_error_message',}),
             "email": forms.TextInput(attrs={'hx-post':'/accounts/check_email/', 'hx-trigger':'keyup', 'hx-target':'#div_error_message',}),

                   }
            



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields 
        


