from django.shortcuts import render

# My Imports 
from django.contrib.auth.decorators import login_required
from .models import Patient
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Function to Render the FrontEnd Page
def frontend(request):
    return render(request, "frontend.html")


# BACKEND SECTION 
# Function to Render the BackEnd Page
@login_required(login_url='login')
def backend(request):
    return render(request, "backend.html")



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

