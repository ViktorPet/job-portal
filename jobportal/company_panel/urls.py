from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view



app_name = 'company_panel'

urlpatterns = [    

    # Employer-only section (matches /company/ pattern)
    path('company/panel/', views.company_panel, name='company_panel'),
    path('company/panel/edit/<int:pk>/', views.edit_job_offer, name='edit_job_offer'),
    path('company/panel/create/', views.create_job_offer, name='create_job_offer'),

]

