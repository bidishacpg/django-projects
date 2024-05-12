from django.http import HttpResponse
from django.shortcuts import render
from job.models import Job
from news.models import News
from contact.models import Contact
from django.core.paginator import Paginator

def homepage(request):

    newsdata=News.objects.all().order_by('news_title')
    jobsdata=Job.objects.all().order_by('job_title')
    data={
        'jobsdata':jobsdata,
        'newsdata':newsdata
        }
       
    return render(request,"homeuser.html",data)

def newsdetails(request):
    newsdetails=News.objects.all()

    dat={
        'newsdetails':newsdetails
    }
    return render(request,"news.html",dat)


def aboutus(request):
    return render(request,"about.html")

def job(request):
    jobdetails=Job.objects.all()
    #paginator= Paginator(jobdetails,2)
    #page_number=request.GET.get('page')
    #jobdetailsfinal=paginator.get_page(page_number)
   # page_obj=paginator.get_page(page_number)


    if request.method=="GET":
       jb =request.GET.get('jobname')
    if jb !=None:
       jobdetails=Job.objects.filter(job_title__icontains= jb)
    data={
        'jobdetails':jobdetails
    }


    #for a in jobdata:
       # print(a.job_title)
       # print(job)
    return render(request,"job.html",data)

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

def saveform(request):
    if request.method=="POST":
      username =request.POST.get('username')
      email =request.POST.get('email')
      mobile =request.POST.get('mobile')
      feedback =request.POST.get('feedback')

      en= Contact(username=username, email=email, mobile=mobile, feedback=feedback)
      en.save()
    return render(request, "saveform.html")



  
   
   