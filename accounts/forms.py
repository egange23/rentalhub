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
            "username": forms.TextInput(attrs={'hx-post': '/accounts/check_username/', 'hx-trigger':'keyup', 'hx-target':'#hint_id_username',}),
             "phone": forms.TextInput(attrs={'hx-post': '/accounts/check_phone/', 'hx-trigger':'keyup', 'hx-target':'#hint_id_phone',}),
             "email": forms.TextInput(attrs={'hx-post':'/accounts/check_email/', 'hx-trigger':'keyup', 'hx-target':'#hint_id_email',}),
                   }          

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields 
        


