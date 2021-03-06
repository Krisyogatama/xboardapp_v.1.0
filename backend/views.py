from wrapper.decorators import unauthenticated_user
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail  
from .utils import searchDashboard, paginateDashboard

from .models import *
from .forms import ProfileForm
from .forms import MemberForm
from .decorators import unauthenticated_user, allowed_users


# Create your views here.

@unauthenticated_user
def loginUser(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboardview')
        else:
            messages.error(request, 'invalid password or username')
            
    return render(request, 'user_login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def requestUser(request):
    return render(request, 'requestuser.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','employees'])
def dashboardview(request):
    dashboardviews, search_query = searchDashboard(request)
    custom_range, dashboardviews = paginateDashboard(request, dashboardviews, 6)

    context = {'dashboardviews': dashboardviews, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'dashboardview.html', context)

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def employeereport(request):
    return render(request, 'employeereport.html')

@login_required(login_url='login')
def mail(request):

    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        recipient = [message_email]
        
        #send an email
        send_mail(
            message_name, #Subject
            message, #Message
            message_email, #From email
            recipient #To email
        )
        
    return render(request, 'mail.html',)

@login_required(login_url='login')
@allowed_users(allowed_roles=['employees', 'admin'])
def profile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'profile.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def member(request):
    members = Member.objects.all()
    
    return render(request, 'member.html', {'members':members})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createuserform(request):
    form = MemberForm

    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('member')

    context = {'form':form}
    return render(request, 'createuserform.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete(request, pk):
    members = Member.objects.get(id=pk).delete()

    return render(request, 'delete.html',  {'members':members})

 