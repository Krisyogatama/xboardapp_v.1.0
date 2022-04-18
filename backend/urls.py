from django.contrib import admin
from django.urls import path
from . import views 
from wrapper import views
from .views import index

urlpatterns = [
    # login and register
    path('user_login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('requestuser/', views.requestUser, name="requestuser"),
    # content
    path('dashboardview/', views.dashboardview, name="dashboardview"),
    path('index/', views.index, name="index"),
    path('employeereport/', views.employeereport, name="employeereport"),
    path('mail/', views.mail, name="mail"),
    path('profile/', views.profile, name="profile"),
    path('member/', views.member, name="member"),
    path('createuserform/', views.createuserform, name="createuserform"),
    path('delete/<str:pk>', views.delete, name="delete")
]   