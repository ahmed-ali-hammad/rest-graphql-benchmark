from patient_info_restapi.views import (AddressViewSet, DoctorViewSet,
                                        EmergencyContactViewSet,
                                        MedicalRecordViewSet,
                                        MedicationViewSet, PatientViewSet)
from rest_framework import routers

app_name = "patient_info_restapi"

router = routers.DefaultRouter()

router.register('patients', PatientViewSet)
router.register('doctors', DoctorViewSet)
router.register('addresses', AddressViewSet)
router.register('emergency_contacts', EmergencyContactViewSet)
router.register('medical_records', MedicalRecordViewSet)
router.register('medications', MedicationViewSet)

urlpatterns = router.urls


