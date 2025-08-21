from django.shortcuts import render
from company_panel.models import JobOffers  
from accounts.models import EmployerProfile, EmployeeProfile


# Create your views here.
def job_list(request):
    user = request.user 
    
    employee = None
    if user.is_authenticated: 
        employee = EmployeeProfile.objects.get(user_id=user.id)
    jobs = JobOffers.objects.all()
    for job in jobs:
        print(job.salary)
    return render(request, 'jobboard/job_list.html', {'jobs': jobs, 'employee': employee })  

def job_detail(request, pk): 
    user = request.user 
    
    employee = None
    if user.is_authenticated: 
        employee = EmployeeProfile.objects.get(user_id=user.id)
    
    job = JobOffers.objects.get(pk=pk) 
    employer_profile = job.company.employerprofile
    return render(request, 'jobboard/job_detail.html', {
        'job': job,
        'company': employer_profile,
        'employee': employee
    })  
    