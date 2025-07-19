from django.urls import path, include
from . import views  

urlpatterns = [
    path('application/', views.submitApplication, name='application')
]