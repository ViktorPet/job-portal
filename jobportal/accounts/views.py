from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, views as auth_views
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, LoginForm, UserEditForm, EmployeeProfileForm,  CustomPasswordChangeForm, EmployerProfileForm
from .models import User, EmployeeProfile, EmployerProfile 
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# Create your views here.

def registerEmployee(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)           
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.role = request.POST.get('role', 'employee')
            new_user.save()
            EmployeeProfile.objects.create(user=new_user)
            return render(request, 'accounts/register_done.html')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'user_form': user_form}) 

def login_user(request):     
    if request.method =="POST":
       form = LoginForm(request.POST)
       if form.is_valid():
           data = form.cleaned_data 
           user = authenticate(
               request, email=data['email'], password=data['password'])
          
           if user is not None :
                login(request, user)
                # Ensure next_url is safe or default to home page
                if user.role == 'employee':
                    return redirect('accounts:employee_edit_profile')
                else: 
                    return redirect('accounts:employer_edit_profile')
                    
           else: 
               return HttpResponse('Invalid credentials')

           
    else:
        form = LoginForm()
    return render(request,'accounts/login_employee.html', {'form': form})

# class MyLogoutView(auth_views.LogoutView):
#     http_method_names = ['get', 'post']

def logout_view(request):
   # If the user is authenticated, retrieve their email and query the DB.
    if request.user.is_authenticated:
        user_email = request.user.email
        try:
            user_instance = User.objects.get(email=user_email)
            username = user_instance.get_full_name()
        except User.DoesNotExist:
            username = ''
    else:
        username = ''

    # Now log the user out
    logout(request)
    messages.info(request, "You have been logged out.")
    
    return render(request, 'accounts/logout.html', {'username': username})   
    
    

def registerEmployer(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.role = request.POST.get('role', 'employer')
            new_user.save()
            EmployerProfile.objects.create(user=new_user)
            return render(request, 'accounts/register_done.html')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/register_employer.html', {'user_form': user_form}) 

@login_required
def employee_edit_profile(request):
    user = request.user
    profile, created = EmployeeProfile.objects.get_or_create(user=user)
    print(user)
    user_form = UserEditForm(instance=user)
    profile_form = EmployeeProfileForm(instance=profile)
    password_form = CustomPasswordChangeForm(user)

    if request.method == 'POST':
        print("POST data:", request.POST)

        if 'update_profile' in request.POST:
            print("Yes")
            user_form = UserEditForm(request.POST, instance=user)
            profile_form = EmployeeProfileForm(request.POST, request.FILES, instance=profile)

            if user_form.is_valid() and profile_form.is_valid():
                print("Submitted email:", request.POST.get('email'))
                print("Current user email:", user.email)
                print("Yes")
                user_form.save()
                profile_form.save()
                messages.success(request, 'Profile updated successfully.')
                return redirect('index')
            else:
                 print("User form errors:", user_form.errors)
                 print("Profile form errors:", profile_form.errors)
        
        elif 'change_password' in request.POST:
            print("Password change branch entered")
            password_form = CustomPasswordChangeForm(user, request.POST)
            user_form = UserEditForm(instance=user)
            profile_form = EmployeeProfileForm(instance=profile)

            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Password changed successfully.')
                return redirect('index')
            else:
                print("Password form errors:", password_form.errors)   

    return render(request, 'accounts/employee_edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'password_form': password_form
    })
    
@login_required
def employer_edit_profile(request): 
    user = request.user
    profile, created = EmployerProfile.objects.get_or_create(user=user)
    print(user)
    profile_form = EmployerProfileForm(instance=profile)
    user_form = UserEditForm(instance=user)
    password_form = CustomPasswordChangeForm(user) 
    
    if request.method == 'POST':
        print("POST data:", request.POST)

        if 'update_profile' in request.POST:
            print("Yes")
            user_form = UserEditForm(request.POST, instance=user)
            profile_form = EmployerProfileForm(request.POST, request.FILES, instance=profile)

            if user_form.is_valid() and profile_form.is_valid():
                print("Yes")
                user_form.save()
                profile_form.save()
                messages.success(request, 'Profile updated successfully.')
                return redirect('index')
            else:
                 print("User form errors:", user_form.errors)
                 print("Profile form errors:", profile_form.errors)
        
        elif 'change_password' in request.POST:
            print("Password change branch entered")
            password_form = CustomPasswordChangeForm(user, request.POST)
            user_form = UserEditForm(instance=user)
            profile_form = EmployeeProfileForm(instance=profile)

            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Password changed successfully.')
                return redirect('index')
            else:
                print("Password form errors:", password_form.errors)   
        
        
    
    return render(request,'accounts/employer_edit_profile.html', 
                  {'user_form': user_form , 
                   'profile_form': profile_form,
                   'password_form': password_form
                   })
