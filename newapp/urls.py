
from django.urls import path
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("dashboard",views.dashboard, name="dashboard"),
    
]