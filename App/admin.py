from django.contrib import admin
from .models import Patient

# Register your models here.
# admin.site.register(Patient)
# or 
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'age', 'gender', 'created_at']
    search_fields = ['name', 'phone', 'email', 'age']
    list_filter = ['gender']
    list_per_page = 2

admin.site.register(Patient, PatientAdmin)
