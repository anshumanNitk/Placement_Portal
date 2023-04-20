from django.shortcuts import render
from django.http import HttpResponse

def UserLogin(request):
    return render(request,'login.html')

def UserSignUp(request):
    return render(request,'signup.html')

# Create your views here.
