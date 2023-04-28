from django.shortcuts import render,redirect
from dashboard.models import CompanyData,inc,Job
from .models import appli
from django.db.models import Count, Max

# Create your views here.

def Application(request):
    com=inc.objects.filter(name='table')[0]
    co=CompanyData.objects.filter(id=com)
    
    for i in co:
        name=i.CompanyName
        roles=i.Roles
        ctc=i.Salary
    en=appli(name=name,roles=roles,ctc=ctc)
    en.save()
    
    
    unique_fields = ['name', 'roles', 'ctc']

    duplicates = (
        appli.objects.values(*unique_fields)
        .order_by()
        .annotate(max_id=Max('id'), count_id=Count('id'))
        .filter(count_id__gt=1)
    )

    for duplicate in duplicates:
        (
            appli.objects
            .filter(**{x: duplicate[x] for x in unique_fields})
            .exclude(id=duplicate['max_id'])
            .delete()
        )
    
    
    company=appli.objects.all()
    return render(request,'application.html',{'company':company})
    