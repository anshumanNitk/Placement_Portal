from django.shortcuts import render,redirect
from .models import CompanyData,Job,inc
from django.contrib.auth.models import User



def DashBoard(request):
    company=CompanyData.objects.all()
    if request.method=='POST':
        job_id=request.POST.get('button')
        inc.objects.filter(name='table').update(val=job_id)
        return redirect('job')
    return render(request,'dashboard.html',{'company':company})


def JobSec(request):
    com=inc.objects.filter(name='table')[0]
    co=CompanyData.objects.filter(id=com)
    for i in co:
        a=i.CompanyName
        b=i.Roles
        c=i.Salary
    if request.method=='POST':
        me=User.objects.filter(username=request.user)
        for i in me:
            name=i.username
        branch=request.POST.get('branch')
        files=request.FILES['file']        
        en=Job(name=name,branch=branch,resume=files,compname=a,roles=b,salary=c)
        en.save()
        return redirect('dashboard')
    return render(request,'JobPage.html',{'co':co})

    
    



