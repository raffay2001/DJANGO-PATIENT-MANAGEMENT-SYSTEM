from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from App import views

urlpatterns = [
    # Native path to access the django-admin.
    path('admin/', admin.site.urls),
    # Path to access the Frontend Page.
    path('' ,views.frontend, name='frontend'),
    # Path to Login / Logout 
    path('login/', include('django.contrib.auth.urls')),

    # BACKEND SECTION 
    path('backend/', views.backend, name='backend'),

    # Path to Add a Pateint 
    path('add_patient/', views.add_patient, name = 'add_patient'),
] 
