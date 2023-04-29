from django.shortcuts import render,redirect
from dashboard.models import Job

# Create your views here.

def Application(request):
    company=Job.objects.filter(name=request.user)
    return render(request,'application.html',{'company':company})
    