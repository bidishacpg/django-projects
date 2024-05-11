from django.db import models
class Job(models.Model):
    job_title=models.CharField(max_length=50)
    job_positions=models.CharField(max_length=50)
    job_details=models.TextField()
    
# Create your models here.
