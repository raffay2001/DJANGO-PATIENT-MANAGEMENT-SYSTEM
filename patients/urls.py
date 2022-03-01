from django import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Native path to access the django-admin.
    path('admin/', admin.site.urls),
    # Path to access the Frontend Page.
    path('', include('App.urls')),
]
