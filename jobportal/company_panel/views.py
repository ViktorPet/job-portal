from django.shortcuts import render, redirect 
from .forms import JobOffersForm
from .models import JobOffers
from django.core.paginator import Paginator

# Create your views here.


def company_panel(request): 
    
    joboffers = JobOffers.objects.filter(company=request.user) 
    
    paginator = Paginator(joboffers, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request,'company_panel/company_panel.html', {'page_obj': page_obj}) 

def create_job_offer(request):
    if request.method == 'POST':
        form = JobOffersForm(request.POST, request.FILES)
        if form.is_valid():
            job_offer = form.save(commit=False)
            job_offer.company = request.user
            job_offer.save()
            return redirect('company_panel:company_panel')
    else:
        form = JobOffersForm()
    return render(request, 'company_panel/edit_job_offers.html', {'job_offers_form': form})


def edit_job_offer(request, pk):
    job_offer = JobOffers.objects.get(pk=pk)

    if request.method == 'POST':
        form = JobOffersForm(request.POST, request.FILES, instance=job_offer)
        if form.is_valid():
            form.save()
            return redirect('company_panel:company_panel')
    else:
        form = JobOffersForm(instance=job_offer)

    return render(request, 'company_panel/edit_job_offers.html', {'job_offers_form': form})

