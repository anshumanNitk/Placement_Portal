from django.shortcuts import render
from .models import CompanyData

def DashBoard(request):
    company=CompanyData.objects.all()
    return render(request,'dashboard.html',{'company':company})
# Create your views here.
