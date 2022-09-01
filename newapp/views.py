from email import message 
from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Contact 

# Create your views here.

def home(request):
    if request.method=='POST':
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        services=request.POST.get("services")
        cleaner=request.POST.get("cleaner")

        info = Contact(name=name, phone=phone, services=services,cleaner=cleaner)
        info.save()

    return render(request, 'Myapp/home.html')

def dashboard(request):
    cmr = Contact.objects.all()
    context={
        'all': cmr
    }
    return render(request, 'Myapp/admin.html', context)
