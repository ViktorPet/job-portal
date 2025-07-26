from django.shortcuts import render
from company_panel.models import JobOffers  
from accounts.models import EmployerProfile


# Create your views here.
def job_list(request):
    jobs = JobOffers.objects.all()
    for job in jobs:
        print(job.salary)
    return render(request, 'jobboard/job_list.html', {'jobs': jobs})  

def job_detail(request, pk):  
    
    job = JobOffers.objects.get(pk=pk) 
    employer_profile = job.company.employerprofile
    return render(request, 'jobboard/job_detail.html', {
        'job': job,
        'company': employer_profile
    })  
    