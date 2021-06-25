"""Online_class URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Project import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('signup_student/', views.Signup_student, name='signup_student'),
    path(r'signup_group/<slug:groupname>',
         views.signup_group, name='signup_group'),
    path('login_student/', views.login, name='login_student'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin', views.admin, name='admin'),
    path(r'group_list/', views.group_list, name='group_list'),
    path(r'group_list/<slug:groupname>',
         views.student_list, name='student_list'),
    path('create_group', views.creategrp, name='create_group'),
    path('logout', views.logout, name='logout')
]
