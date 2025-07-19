from django.core.exceptions import ValidationError

def clean_and_validate_email(email, model_class, instance_pk=None, error_message="This email already exists."): 
    

    cleaned_email = email.strip().lower()

    queryset = model_class.objects.filter(email__iexact=cleaned_email)
    if instance_pk:
        queryset = queryset.exclude(pk=instance_pk)

    if queryset.exists():
        raise ValidationError(error_message)

    return cleaned_email
