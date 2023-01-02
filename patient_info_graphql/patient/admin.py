from django.contrib import admin
from patient.models import Patient, Doctor

admin.site.register(Patient)

admin.site.register(Doctor)