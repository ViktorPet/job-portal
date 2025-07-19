from django.shortcuts import render
import requests
from django.conf import settings 
from external_api.views import get_reed_jobs 
from accounts.models import EmployeeProfile, EmployerProfile
import json

# Create your views here.

def index(request): 
    
    print(request.user.role) 
    
    user = request.user
    
    if request.user.role == "employer":  
        profile = EmployerProfile.objects.get(user_id=user.id)
    else:  
        profile = EmployeeProfile.objects.get(user_id=user.id)
        
    
    
    
    jobs_data = get_reed_jobs(query='django developer')  # Call the function directly

    if jobs_data:
        jobs = jobs_data.get('results', [])  # Get the list of jobs safely
        # print(jobs)
    else:
        jobs = []
        
    return render(request, 'core/index.html', { 'jobs': jobs, 'profile': profile})