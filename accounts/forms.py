from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUser, CustomGroup

class TextInput(forms.TextInput):
    input_type: 'str'




class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("organization","email",)

    def clean_email(self, *args, **kwargs):

        custom_group = CustomGroup.objects.all()
        domains_list = [group.domain for group in custom_group]
        domains_tuple = tuple(domains_list)
        accepted_domains = (domains_tuple)
        if len(accepted_domains) == 0:
            accepted_domains = ("@hotmail.com")


        email = self.cleaned_data.get("email")
        email = email.casefold()
        if email.endswith(accepted_domains):
            return email
        else:
            raise forms.ValidationError("Hmmmmm, maybe you need to change this into your organizations email domain. Or worst, your organization has not been approved to use this app")
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields 
        
class CustomGroupForm(forms.ModelForm):
    class Meta:
        model = CustomGroup
        fields = "__all__"
        
        widgets = {
            "name":TextInput(attrs={'placeholder':"Enter name of the organization",}),
            "domain":TextInput(attrs={'placeholder':"Example: gmail.com, health.nsw.gov.au",})
        }
    def clean_domain(self,*args, **kwargs):
        domain = self.cleaned_data.get("domain")
        domain = domain.casefold()
        if domain.find("@") == 0 and domain.find(".") > 2:
            return domain
        else:
            raise forms.ValidationError("please enter a valid domain starting with '@' ")

    def clean_name(self, *args, **kwargs):
        name= self.cleaned_data.get("name").casefold()
        return name

