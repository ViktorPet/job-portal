from django.shortcuts import render
import requests
from django.conf import settings 
from external_api.views import get_reed_jobs 
from accounts.models import EmployeeProfile, EmployerProfile
import json

# Create your views here.

def index(request): 
    user = request.user
    
    # Initialize profile as None
    profile = None 
    
    print(user)

    if user.is_authenticated:
        try:
            if hasattr(user, 'role') and user.role == "employer":  
                profile = EmployerProfile.objects.get(user_id=user.id)
            else:  
                profile = EmployeeProfile.objects.get(user_id=user.id)
        except (EmployerProfile.DoesNotExist, EmployeeProfile.DoesNotExist):
            profile = None  # Handle missing profile gracefully
    else:
        # Optionally redirect to login page
        # return redirect('login')
        pass

    jobs_data = get_reed_jobs(query='django developer')

    if jobs_data:
        jobs = jobs_data.get('results', [])
    else:
        jobs = []

    return render(request, 'core/index.html', { 'jobs': jobs, 'profile': profile })
