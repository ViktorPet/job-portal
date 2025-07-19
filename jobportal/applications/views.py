from django.shortcuts import render, redirect
from .models import Application
from .forms import ApplicationForm
from django.contrib.auth.decorators import login_required

@login_required
def submitApplication(request): 
    user = request.user
    
    try:
        instance = Application.objects.get(user=user)
    except Application.DoesNotExist:
        instance = None

    if request.method == 'POST':
        print("Form submitted")  # ✅ You should now see this
        form = ApplicationForm(request.POST, request.FILES, instance=instance)
        
        if form.is_valid():
            application = form.save(commit=False)
            application.user = user
            application.save()
            return redirect('index')
        else:
            print("Form errors:", form.errors)
    else:
        form = ApplicationForm(instance=instance)

    return render(request, 'applications/application.html', {"form": form})
