from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class CustomGroup(models.Model):
    name = models.CharField(max_length=150, unique=True)
    domain = models.CharField(max_length=150, unique=True)
    date_joined = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True,)
    organization = models.ForeignKey(CustomGroup, on_delete=models.CASCADE, null=True, blank=True,)
    city = models.CharField(max_length=250, blank=True, null=True)
    state = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    email = models.EmailField(unique=True)
    manager = models.BooleanField(default=True)
    works_where = models.ManyToManyField(CustomGroup, related_name="works_where")
      
    def __str__(self):
        return  self.username
 
class SocialMedia(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    facebook = models.CharField(default = "#", max_length=250, blank=True, null=True)
    instagram = models.CharField(default = "#", max_length=250, blank=True, null=True)
    snapchat = models.CharField(default = "#", max_length=250, blank=True, null=True)
    pinterest = models.CharField(default = "#", max_length=250, blank=True, null=True)
    twitter = models.CharField(default = "#", max_length=250, blank=True, null=True)
    linkedin = models.CharField(default = "#", max_length=250, blank=True, null=True)

    def __str__(self):
        return  str(self.user)



    
    