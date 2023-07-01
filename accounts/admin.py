from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import *

from .models import *



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "first_name",
        "last_name",
        "email",
        "phone",
        
    ]

    fieldsets = UserAdmin.fieldsets + ((None, {"fields":("phone",)}),)
    add_fieldsets = UserAdmin.fieldsets + ((None, {"fields":("phone",)}),)




admin.site.register(CustomUser, CustomUserAdmin)
