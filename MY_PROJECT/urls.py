"""MY_PROJECT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app.views import *
from django.views.generic import TemplateView







urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',TemplateView.as_view(template_name="home.html"),name='home'),
    path('welcome/',TemplateView.as_view(template_name="welcome.html"),name='welcome'),
    path('python/',TemplateView.as_view(template_name="python.html"),name='python'),
    path('java/',TemplateView.as_view(template_name="java.html"),name='java'),
    path('mern/',TemplateView.as_view(template_name="mern.html"),name='mern'),
    path('register/',register,name='register'),
    path('forget_password/',forget_password,name='forget_password'),
    path('change_password/',change_password,name='change_password'),
    path('student_data/',student_data,name='student_data'),
    path('user_login/',user_login,name='user_login'),
    path('user_logout/',user_logout,name='user_logout'),
    

]
