"""
URL configuration for mobile_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, include
from authorization_app import views as auth_views
from main_app import views as main_views

urlpatterns = [
    path('', auth_views.auth_screen, name='auth'),
    path('registration/', auth_views.reg_screen, name='registration'),
    path('main/', main_views.main_screen, name='main'),
    
]
