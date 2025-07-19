from django.shortcuts import render
from company_panel.models import JobOffers


# Create your views here.
def job_list(request):
    jobs = JobOffers.objects.all()
    for job in jobs:
        print(job.salary)
    return render(request, 'jobboard/job_list.html', {'jobs': jobs})  

def job_detail(request):   
    pass