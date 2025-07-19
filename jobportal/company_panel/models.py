from django.db import models
from ckeditor.fields import RichTextField 
from accounts.models import User 
from ckeditor.fields import RichTextField 

JOB_TYPE_CHOICES = [
    ('full-time', 'Full Time'),
    ('part-time', 'Part Time'),
    ('internship', 'Internship'),
]

JOB_PLACE_CHOICES = [
    ('remote', 'Remote'),
    ('on-site', 'On Site'),
    ('hybrid', 'Hybrid'),
]

class JobOffers(models.Model): 
    company = models.ForeignKey(User,on_delete=models.CASCADE, limit_choices_to={'role': 'employer'}, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True) 
    description = RichTextField() 
    location = models.CharField(max_length=255, blank=True, null=True)
    salary = models.DecimalField(max_digits=10,decimal_places=2, blank=True, null=True)
    published = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    jobtype = models.CharField(
        max_length=20, 
        choices=JOB_TYPE_CHOICES, 
        default='full-time', 
        blank=True
    )
    jobplace = models.CharField(
        max_length=20, 
        choices=JOB_PLACE_CHOICES, 
        default='on-site', 
        blank=True
    )
    
    
    def __str__(self):
        return self.title