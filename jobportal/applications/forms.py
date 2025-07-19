from django import forms
from .models import Application
from jobportal.helpers import clean_and_validate_email  # ✅ correct import


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = (
            'firstname', 'lastname', 'email', 'birthday', 
            'education', 'gender', 'year_of_graduation', 'skills',
            'desired_salary', 'applicant_photo', 'applicant_cv',
            'languages', 'website'
        )
        widgets = {
            'year_of_graduation': forms.DateInput(attrs={'type': 'date'}),
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-select'}, choices=[('', 'Select Gender')] + list(Application._meta.get_field('gender').choices))
        
        }

    def clean_email(self):  # ✅ method must be inside the class
        email = self.cleaned_data.get('email', '')
        return clean_and_validate_email(
            email=email,
            model_class=Application,
            instance_pk=self.instance.pk,
            error_message="An application with that email already exists."
        )
