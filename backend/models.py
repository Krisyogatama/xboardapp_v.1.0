from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200, null=True)
    Phone = models.CharField(max_length=200, null=True)
    Email = models.CharField(max_length=200, null=True)
    Job_Title = models.CharField(max_length=200, null=True)
    Street = models.CharField(max_length=200, null=True)
    City = models.CharField(max_length=200, null=True)
    State = models.CharField(max_length=200, null=True)
    Province = models.CharField(max_length=200, null=True)
    Profile_pic = models.ImageField(default="Metrocom.png", null=True, blank=True)
    Date_Created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.Name)

class Member(models.Model):
    
    Name = models.CharField(max_length=200, null=True)
    Job_Title = models.CharField(max_length=200, null=True)
    Email = models.CharField(max_length=200, null=True)
    Unit = models.CharField(max_length=200, null=True)
    Status = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.Name

class Dashboardview(models.Model):
    project_name = models.CharField(max_length=200, null=True)
    bi_software = models.CharField(max_length=200, null=True)
    dashboard_title = models.CharField(max_length=200, null=True)
    icon_pic = models.ImageField(default="Metrocom.png", null=True, blank=True)
    link_iframe = models.CharField(max_length=200, null=True)
    Date_Created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.project_name

