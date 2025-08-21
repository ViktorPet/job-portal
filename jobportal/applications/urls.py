from django.urls import path, include
from . import views  

urlpatterns = [
    path('application/<int:job_id>', views.submitApplication, name='application')
]