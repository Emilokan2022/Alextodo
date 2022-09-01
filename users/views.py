from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login



# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST.get ('username')
        firstname = request.POST.get ('firstname')
        lastname = request.POST.get ('lastname')
        email = request.POST.get ('email')
        password = request.POST.get ('password')
        confirmpassword = request.POST.get ('password2')


        if password != confirmpassword:
            messages.error(request,"your password does not match")
            return redirect('register')

        if User.objects.filter(username=username):
            messages.error(request,'this username already exist')
            return redirect('register')

        if User.objects.filter(email=email):
            messages.error(request,'this email already exist')
            return redirect('register')
        if len(username)>15:
            messages.error(request,'this username should be lessee than 15')
            return redirect('register')





        user = User.objects.create_user(username,email,password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        messages.success(request, "your details have been succesfully registered")
        return redirect('login')
    
    return render (request,'users/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get ('username')
        password = request.POST.get ('password')

        user= authenticate(username=username,password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "you have succesfully logged in")
          
            return redirect('Myapp:home')
        else:
            messages.error(request, "wrong username or password")
            return redirect('login')
    return render (request,'users/login.html')


def leave(request):
    logout(request)
    return redirect('/login')