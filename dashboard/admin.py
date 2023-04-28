from django.contrib import admin

from .models import CompanyData

from .models import Job,inc
admin.site.register(CompanyData)
admin.site.register(Job)
admin.site.register(inc)
# Register your models here.
