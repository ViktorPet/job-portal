from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts.managers import CustomUserManager
from django.conf import settings



ROLE = (
    ('employer', "Employer"),
    ('employee', "Employee"),
)



class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True )
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    role = models.CharField(choices=ROLE,  max_length=10)
    


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name+ ' ' + self.last_name
    objects = CustomUserManager()


class EmployeeProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Basic Information
    phone_number = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='profile_employee_photos/', null=True, blank=True)

    # Experience and Skills
    experience = models.TextField(blank=True)  # Rich experience description
    skills = models.TextField(blank=True)

    # Education
    education = models.TextField(blank=True)

    # Languages
    languages = models.TextField(blank=True)

    # Work Preferences
    preferred_job_title = models.CharField(max_length=255, blank=True)
    preferred_location = models.CharField(max_length=255, blank=True)
    salary_expectation = models.CharField(max_length=100, blank=True)

    # Courses / Certifications
    certifications = models.TextField(blank=True)

    # Additional Info
    additional_info = models.TextField(blank=True)
    
    # Willing to move closer to work
    willing_to_move = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.company_name} Profile"

class EmployerProfile(models.Model):
    
    

    
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_eik = models.IntegerField(blank=True, null=True)
    company_country = models.CharField(max_length=255, blank=True, null=True)
    company_address_street = models.CharField(max_length=255, blank=True, null=True)
    company_address_town = models.CharField(max_length=255, blank=True, null=True)
    company_phone_number = models.CharField(max_length=20, blank=True, null=True)
    company_address_postcode = models.CharField(max_length=255, blank=True, null=True)
    company_website = models.URLField( blank=True, null=True)
    type_of_business = models.CharField(max_length=255, blank=True, null=True)
    company_description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True)
    company_picture = models.ImageField(upload_to='company_pictures/', blank=True)
    
    def __str__(self):
        return self.company_name