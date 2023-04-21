from django.db import models

class SignUpStat(models.Model):
    username=models.CharField(max_length=50,null=False)
    branch=models.CharField(max_length=25,null=False)
    mail=models.EmailField()
    
    
    
    def __str__(self):
        return self.username + '- ' + self.branch



