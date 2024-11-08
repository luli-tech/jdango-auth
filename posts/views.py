from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Features

def Home(request):
    features=Features.objects.all()
    return render(request,'posts/index.html',{'features':features})
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('/')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username already used')
                return redirect('/')  
            else:
                user=User.objects.create_user(username=username,email=email,password=password)  
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password does not match') 
            return redirect(request,'register')
    return render(request,'posts/register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'credentials invalid')
            return redirect('login')
    else: 
         return render(request,'posts/login.html')
    
def logout(request):
     auth.logout(request)
     return redirect('/')