from django.http import HttpResponse
from django.shortcuts import render
from job.models import Job

def homepage(request):
    jobsdata=Job.objects.all()
    data={
        'jobsdata':jobsdata
        }
       
    return render(request,"homeuser.html",data)

def aboutus(request):
    return render(request,"about.html")

def job(request):


    #for a in jobdata:
       # print(a.job_title)
       # print(job)
    return render(request,"job.html")

def userform(request):
    finalans=0
    try:
        #n1=int(request.GET['num1'])
        #n2=int(request.GET['num2'])

        n1=int(request.POST.get('num1'))
        n2=int(request.POST.get('num2'))

        finalans=n1+n2

        #print(n1+n2);
    except:
        pass
    return render(request,"userform.html",{'output':finalans})


  
   
   