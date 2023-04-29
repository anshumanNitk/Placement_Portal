from django.contrib import admin

from .models import CompanyData

from .models import inc,Job
admin.site.register(CompanyData)
admin.site.register(inc)
admin.site.register(Job)
# Register your models here.
