"""demo URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
path('',views.index),

path('signup',views.handleSignup,name='handleSignup'),
path('logout',views.handlelogout,name='handlelogout'),
path('login', views.handlelogin, name='login'),
path('home',views.home,name='home'),
path('nothome',views.nothome,name='nothome'),
path('out', views.out, name='out'),
path('users', views.users, name='users'),
path('profile',views.profile,name='profile')

]