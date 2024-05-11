from django.db import models
from tinymce.models import HTMLField
class Job(models.Model):
    job_title=models.CharField(max_length=50)
    job_positions=models.CharField(max_length=50)
    job_details=HTMLField()
    
# Create your models here.
