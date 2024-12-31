from django.contrib import admin
from patient_info_graphql.models import (
    Address,
    Allergy,
    Doctor,
    EmergencyContact,
    Illness,
    MedicalRecord,
    Medication,
    Patient,
    Surgery,
)

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(EmergencyContact)
admin.site.register(Address)
admin.site.register(MedicalRecord)
admin.site.register(Medication)
admin.site.register(Illness)
admin.site.register(Allergy)
admin.site.register(Surgery)
