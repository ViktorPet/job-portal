from django.db import models
from django.conf import settings


# Create your models here.  

class GenderChoices(models.TextChoices):
    MALE = 'Male', 'Male'
    FEMALE = 'Female', 'Female'


class Application(models.Model): 
    firstname = models.CharField(max_length=150, blank=True)
    lastname = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True, blank=False,error_messages={'unique': "An application with that email already exists.",})
    birthday = models.DateField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices, null=True)
    education = models.TextField(blank=True)
    year_of_graduation = models.DateField()
    skills = models.TextField(blank=True)
    desired_salary = models.IntegerField(blank=True)
    languages = models.TextField(blank=True)
    applicant_photo = models.ImageField(upload_to='aplicants_photos/', null=True, blank=True)
    applicant_cv = models.FileField(max_length=255,upload_to ='uploads/%Y/%m/%d/')
    website = models.URLField(max_length=200)

def __str__(self):
        return self.email

def get_full_name(self):
    return self.firstname+ ' ' + self.lastname



    