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



def Manage(request):
    man=CompanyData.objects.filter(poc=request.user)
    for i in man:
        b=i.CompanyName
    if request.method=='POST':
        name=request.POST.get('companyname')
        roles=request.POST.get('roles')
        salary=request.POST.get('salary')
        start=request.POST.get('start')
        end=request.POST.get('end')
        description=request.POST.get('description')
        CompanyData.objects.filter(CompanyName=name).update(Roles=roles,Salary=salary,TimeStart=start,TimeEnd=end,Description=description)
    jj=Job.objects.filter(compname=b)
    return render(request,'manage.html',{'compan':man,'job':jj})
    
    



