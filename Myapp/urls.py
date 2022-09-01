from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from . import views


app_name="Myapp"


urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('pricing/', views.pricing, name="pricing"),
    path('services/', views.services, name="services"),
    
    
]
