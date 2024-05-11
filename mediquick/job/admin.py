from django.contrib import admin
from job.models import Job
class jobadmin(admin.ModelAdmin):
    list_display=('job_title','job_positions','job_details')
admin.site.register(Job,jobadmin)
# Register your models here.
