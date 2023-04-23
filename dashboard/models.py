from django.db import models

class CompanyData(models.Model):
    CompanyName=models.CharField(max_length=50,null=False)
    Description=models.TextField()
    Roles=models.CharField(max_length=50,null=False)
    Salary=models.CharField(max_length=50,null=False)
    TimeStart=models.DateTimeField(auto_now=False, auto_now_add=False)
    TimeEnd=models.DateTimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        
        return self.CompanyName