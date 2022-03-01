from django.shortcuts import render

# Function to Render the FrontEnd Page
def frontend(request):
    return render(request, "frontend.html")


# Function to Render the BackEnd Page
def backend(request):
    return render(request, "backend.html")
