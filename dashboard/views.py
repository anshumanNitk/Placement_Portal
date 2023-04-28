from django.shortcuts import render,redirect
from .models import CompanyData,Job,inc



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
    if request.method=='POST':
        name=request.POST.get('name')
        branch=request.POST.get('branch')
        files=request.FILES['file']        
        en=Job(name=name,branch=branch,resume=files)
        en.save()
        return redirect('dashboard')
    return render(request,'JobPage.html',{'co':co})

    
    



