from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from . import views

app_name="userapp"


urlpatterns = [

    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('leave/', views.leave, name="leave"),

]