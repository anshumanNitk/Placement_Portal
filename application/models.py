from django.db import models

# Create your models here.
class appli(models.Model):
    name=models.CharField(max_length=50)
    roles=models.CharField(max_length=50)
    ctc=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    class meta:
        unique_together = ["name", "roles", "ctc"]
