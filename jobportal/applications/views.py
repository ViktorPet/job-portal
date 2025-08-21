from django.shortcuts import render, redirect
from accounts.models import EmployeeProfile, User
from .forms import ApplicationForm
from django.contrib.auth.decorators import login_required 
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


@login_required
def submitApplication(request, job_id):
    user = request.user
    profile = getattr(user, 'employeeprofile', None)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            print("✅ Form is valid")
            application = form.save(commit=False)
            application.job_id = job_id
            application.user = user
            application.save()
            # send_mail(
            #     "Test Subject from Django",
            #     "This is a test email using Brevo SMTP.",
            #     "victor.data.host@gmail.com",  # From
            #     ["viktor_petrovvt@abv.bg"], # To
            #     fail_silently=False, 
            # )
            send_email_toapplicant(user)
            print("💾 Application saved")
            return redirect('index')
        else:
            print("❌ Form is NOT valid")
            print(form.errors)  # Show in console
    else:
        initial_data = {
            'firstname': user.first_name,
            'lastname': user.last_name,
            'email': user.email,
        }
        if profile:
            initial_data.update({
                'birthday': profile.date_of_birth,
                'education': profile.education,
                'skills': profile.skills,
                'languages': profile.languages,
                'desired_salary': profile.salary_expectation,
                'website': getattr(profile, 'website', '')  # if exists
            })

        form = ApplicationForm(initial=initial_data)

    return render(request, 'applications/application.html', {"form": form})


def send_email_toapplicant(user): 
    context = {
        "email": user.email,
        "firstname": user.first_name,
        "lastname": user.last_name,
    }

    # HTML content (inside the function)
    msg_html = render_to_string("applications/emails/email.html", context)

    # Plain text fallback (optional)
    msg_plain = "Hello {0} {1},\n\nThank you for your application. We’ll contact you soon!".format(
        user.first_name, user.last_name
    )

    send_mail(
        subject="Your application was submitted!",
        message=msg_plain,   # fallback if email client doesn't support HTML
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        html_message=msg_html,  # HTML version
    )
