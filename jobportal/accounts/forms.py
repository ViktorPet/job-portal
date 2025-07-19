from django import forms
from .models import User, EmployeeProfile , EmployerProfile
from django.contrib.auth.forms import PasswordChangeForm 
from jobportal.helpers import clean_and_validate_email  # import helper


class LoginForm(forms.Form): 
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [ 'first_name','last_name', 'email', 'role']

    def check_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Passwords do not match')
        return self.cleaned_data['password2'] 
    
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email') 
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        print("Cleaned email in form:", email)
        if not email:
            return email  # allow empty emails if not required

        qs = User.objects.filter(email=email).exclude(pk=self.instance.pk)
        print("QuerySet result:", qs)
        if qs.exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

    
class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        exclude = ('user',) 
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            # add widgets for other fields as needed
        }
        
class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'}) 
            
class EmployerProfileForm(forms.ModelForm): 
    class Meta: 
        model = EmployerProfile 
        exclude = ('user',)