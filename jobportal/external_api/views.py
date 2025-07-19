from django.shortcuts import render
import requests
from django.conf import settings
from django.http import JsonResponse
from external_api.utils import get_reed_auth_header
import json



def get_reed_jobs(query='python developer', location='london', results_to_take=10):
    url = "https://www.reed.co.uk/api/1.0/search"
    headers = get_reed_auth_header()
    params = {
        "keywords": query,
        "locationName": location,
        "resultsToTake": results_to_take
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None
    
def jobs_search(request):
    jobs = get_reed_jobs(query='django developer')
    return JsonResponse(jobs)

