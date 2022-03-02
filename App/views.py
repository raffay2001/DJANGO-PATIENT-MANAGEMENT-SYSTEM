from django.shortcuts import render

# My Imports 
from django.contrib.auth.decorators import login_required

# Function to Render the FrontEnd Page
def frontend(request):
    return render(request, "frontend.html")


# BACKEND SECTION 
# Function to Render the BackEnd Page
@login_required(login_url='login')
def backend(request):
    return render(request, "backend.html")
    