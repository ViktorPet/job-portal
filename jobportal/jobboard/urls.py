from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('jobs', views.job_list, name='job_list'),
    path('<int:pk>/', views.job_detail, name='job_detail'),
]
