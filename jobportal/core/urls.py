from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view



urlpatterns = [
    path('', views.index, name='index'),    
   
]
