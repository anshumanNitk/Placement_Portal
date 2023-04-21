from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import SignUpStat

def UserLogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,'bad credentials!')
    return render(request,'login.html')

def UserSignUp(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('Email')
        branch=request.POST.get('branch')
        password=request.POST.get('password')
        
        ln=SignUpStat(username=username,mail=email,branch=branch)
        ln.save()
        
        en=User.objects.create_user(username,email,password)
        en.save()
        messages.success(request,'sucessfully signed up!')
        
        return redirect('login')        
    else:   
        return render(request,'signup.html')

# Create your views here.
