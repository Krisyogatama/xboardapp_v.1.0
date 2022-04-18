from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


from .models import *

#model forms 

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
