from django.db import models
from django.contrib.auth.models import User

class CompanyData(models.Model):
    CompanyName=models.CharField(max_length=50,null=False)
    Description=models.TextField(null=False)
    Roles=models.CharField(max_length=50,null=False)
    Salary=models.CharField(max_length=50,null=False)
    TimeStart=models.DateTimeField(auto_now=False, auto_now_add=False)
    TimeEnd=models.DateTimeField(auto_now=False, auto_now_add=False)
    poc=models.ForeignKey(User,default=None,on_delete=models.DO_NOTHING,unique=True)
    
    def __str__(self):
        
        return self.CompanyName 
    
    
class inc(models.Model):
    name=models.CharField(default='',max_length=50)
    val=models.IntegerField(null=False,primary_key=True,default='')
    def __int__(self):
        return self.val
    
class Job(models.Model):
    name=models.CharField( max_length=50,default=None)   
    branch=models.CharField( max_length=50,default=None) 
    resume=models.FileField(null=False,max_length=250,default=None)
    compname=models.CharField(max_length=50,default=None)
    roles=models.CharField(max_length=50,default=None)
    salary=models.CharField(max_length=50,default=None)
        
    
    def __str__(self):
        return self.compname