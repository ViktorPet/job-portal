from django.contrib import admin
from django.core.mail import send_mass_mail
from django.conf import settings
from .models import MassEmails
from accounts.models import User   # adjust depending on where your User model is

@admin.register(MassEmails)
class MassEmailsAdmin(admin.ModelAdmin):
    list_display = ('subject', 'user_type', 'published')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        # Select users based on type
        if obj.user_type == 'employer':
            recipients = User.objects.filter(role='employer').values_list('email', flat=True)
        elif obj.user_type == 'employee':
            recipients = User.objects.filter(role='employee').values_list('email', flat=True)
        else:
            recipients = User.objects.all().values_list('email', flat=True)

        # Prepare messages
        messages = [
            (obj.subject, obj.body, settings.DEFAULT_FROM_EMAIL, [email])
            for email in recipients
        ]
        
        # Send emails
        if messages:
            send_mass_mail(messages, fail_silently=False)