from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import *

from .models import *
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "city",
        "state",
        
    ]
    
    # fieldsets = UserAdmin.fieldsets + ((None, {"fields":("",)}),)
    # add_fieldsets = UserAdmin.fieldsets + ((None, {"fields":("",)}),)
    fieldsets = UserAdmin.fieldsets + ((None, {"fields":("city","state","phone", "organization")}),)
    add_fieldsets = UserAdmin.fieldsets + ((None, {"fields":("state","state", "phone","organization")}),)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomGroup)
admin.site.register(SocialMedia)