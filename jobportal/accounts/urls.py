from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view

app_name = 'accounts'

# urlpatterns = [    
#     path('register/', views.registerEmployee, name='register'),
#     path('register_employer/', views.registerEmployer, name='register_employer'),
#     path('profile/', views.employee_edit_profile, name='employee_edit_profile'),
#     path('profile_employer/', views.employer_edit_profile, name='employer_edit_profile'),
#     path('change-password/', views.employee_edit_profile, name='password_change'),
#     path('login/', views.login_user, name='login'),
#     # path('login_employer/', views.login_employer, name='login_employer'),
#     path('logout/', views.logout_view, name='logout'),  
   
# ]

urlpatterns = [    
    # Public routes
    path('register/', views.registerEmployee, name='register'),
    path('register/employer/', views.registerEmployer, name='register_employer'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Employee-only section
    path('profile/', views.employee_edit_profile, name='employee_edit_profile'),
    path('profile/change-password/', views.employee_edit_profile, name='password_change'),

    # Employer-only section (matches /company/ pattern)
    path('company/profile/', views.employer_edit_profile, name='employer_edit_profile'),
]

