from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import *

from .models import *



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = ContactVerificationForm
    model = CustomUser
    list_display = [
        "username",
        'phone',
        'email_verification_code',
        'email_verified',
        'phone_verification_code',
        'phone_verified',
         'is_staff',
        'is_active',
        'date_joined',

    ]
    
    # variables = CustomUser.__dict__.keys()
    # for variable in variables: 
    #     list_display.append(variable)
    # print(list_display)

    fieldsets = UserAdmin.fieldsets + ((None, {"fields":("phone",        'email_verification_code',
        'email_verified',
        'phone_verification_code',
        'phone_verified',)}),)
    add_fieldsets = UserAdmin.fieldsets + ((None, {"fields":("phone",)}),)




admin.site.register(CustomUser, CustomUserAdmin)
