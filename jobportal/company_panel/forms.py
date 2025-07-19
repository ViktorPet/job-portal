from  django import forms
from .models import JobOffers
from ckeditor.widgets import CKEditorWidget 
from django.utils.translation import gettext_lazy as _
 


class JobOffersForm(forms.ModelForm): 
    description = forms.CharField(widget=CKEditorWidget(config_name='full'), label=_('Content')) 
    
    class Meta: 
        model = JobOffers
        fields = '__all__'
