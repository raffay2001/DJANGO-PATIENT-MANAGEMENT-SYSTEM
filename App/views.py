from django.shortcuts import render

# My Imports 
from django.contrib.auth.decorators import login_required
from .models import Patient
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator

# Function to Render the FrontEnd Page
def frontend(request):
    return render(request, "frontend.html")


# BACKEND SECTION 
# Function to Render the BackEnd Page
@login_required(login_url='login')
def backend(request):
    # if its a GET request 
    if 'q' in request.GET:
        q = request.GET['q']
        all_patient_list = Patient.objects.filter(
            Q(name__icontains=q) | Q(phone__icontains=q) | Q(email__icontains=q) | Q(age__icontains=q) |  Q(gender__icontains=q) |   Q(note__icontains=q) 
        ).order_by('-created_at')
    else:
        all_patient_list = Patient.objects.all().order_by('-created_at')
    paginator = Paginator(all_patient_list, 3)
    page = request.GET.get('page')
    all_patient = paginator.get_page(page)

    return render(request, 'backend.html', {"patients": all_patient})




# Function to Add the Pateint 
@login_required(login_url='login')
def add_patient(request):
    # if its a POST request 
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('age') and request.POST.get('gender') or request.POST.get('note'):
            patient = Patient()
            patient.name = request.POST.get('name')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.note = request.POST.get('note')
            patient.save()
            messages.success(request, "Patient Added Successfully !")
            # Redirecting the user to the backend page 
            return HttpResponseRedirect(reverse('backend'))
    
    # if its a GET request
    else:
        return render(request, 'add.html')

