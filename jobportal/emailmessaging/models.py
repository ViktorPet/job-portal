from django.db import models
from ckeditor.fields import RichTextField   # if you’re using CKEditor for RichText

class MassEmails(models.Model): 
    USER_TYPE_CHOICES = (
        ('employer', 'Employer'),
        ('employee', 'Employee'),
        ('all', 'All Users'),
    )
    
    subject = models.CharField(max_length=255, blank=True, null=True) 
    body = RichTextField()
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='all')
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} ({self.user_type})"
