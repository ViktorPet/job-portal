from django.urls import path, include
from . import views




urlpatterns = [
    path('search/', views.jobs_search, name='jobs_search'),    
   
]
