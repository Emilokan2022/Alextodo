from multiprocessing import context
from wsgiref.util import request_uri
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Contact
from django.contrib.auth.decorators import login_required


# Create your views here.

# def index(request):
#     counter = request.POST['count']
#     total_number = len(counter.split())
#     context = {
#         'amount': total_number,
#     }


#     return render(request, 'myapp/index.html',context)






# def about(request):

#     return render(request, 'myapp/about.html')


@login_required
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        info = Contact(name=name,email=email,phone=phone,message=message)                                   
        info.save()

    
    return render(request, 'Myapp/home.html')












def dashboard(request):
    crm = Contact.objects.all()
    context = {
        'all':crm

    }
    return render(request, 'Myapp/admin.html', context)

def update(request, id):
    tel =Contact.objects.get(id=id)

    if request.method == 'POST':
        tel.name=request.POST.get("name")
        tel.email=request.POST.get("email")
        tel.phone=request.POST.get("phone")
        tel.message=request.POST.get("message")
        tel.save()
        return redirect('/dashboard')

    context ={
        'call':tel

    }

    return render(request, 'Myapp/update.html', context)



def delete(request, id):
    dels= Contact.objects.get(id=id)
    dels.delete()
    return redirect('/dashboard')

def pricing(request):

    return render(request, 'Myapp/pricing.html')

def services(request):

    return render(request, 'Myapp/services.html')

def Images(request):
    return render(request, 'Myapp/images.html')
