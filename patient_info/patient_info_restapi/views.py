from django.shortcuts import get_object_or_404
from patient_info_graphql.models import (Address, Doctor, EmergencyContact,
                                         MedicalRecord, Medication, Patient)
from patient_info_restapi.serializers import (AddressSerializer,
                                              DoctorSerializer,
                                              EmergencyContactSerializer,
                                              MedicalRecordSerializer,
                                              MedicationSerializer,
                                              PatientSerializer,
                                              VerifyPatientIDSerializer)
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class EmergencyContactViewSet(ModelViewSet):
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencyContactSerializer

    @action(detail=False, methods=['post'], serializer_class=VerifyPatientIDSerializer)
    def get_patient_emergency_contact(self, request):
        serializer = VerifyPatientIDSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        emergency_contact = get_object_or_404(Patient, id=request.data.get('patient_id')).emergency_contact

        return Response(EmergencyContactSerializer(emergency_contact).data, status=status.HTTP_200_OK)


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    @action(detail=False, methods=['post'], serializer_class=VerifyPatientIDSerializer)
    def get_patient_address(self, request):
        serializer = VerifyPatientIDSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        address = get_object_or_404(Patient, id=request.data.get('patient_id')).address

        return Response(AddressSerializer(address).data, status=status.HTTP_200_OK)


class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    @action(detail=False, methods=['post'], serializer_class=VerifyPatientIDSerializer)
    def get_patient_associated_doctor(self, request):
        serializer = VerifyPatientIDSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        doctor = get_object_or_404(Patient, id=request.data.get('patient_id')).primary_care_physician

        return Response(DoctorSerializer(doctor).data, status=status.HTTP_200_OK)


class MedicalRecordViewSet(ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer

    @action(detail=False, methods=['post'],  serializer_class=VerifyPatientIDSerializer)
    def get_patient_medical_records(self, request):
        serializer = VerifyPatientIDSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        medical_records = get_object_or_404(Patient, id=request.data.get('patient_id')).medical_records.all()

        return Response(MedicalRecordSerializer(medical_records, many=True).data, status=status.HTTP_200_OK)


class MedicationViewSet(ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

    @action(detail=False, methods=['post'],  serializer_class=VerifyPatientIDSerializer)
    def get_patient_medication(self, request):
        serializer = VerifyPatientIDSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        medical_records = get_object_or_404(Patient, id=request.data.get('patient_id')).medical_records.select_related('illnesses', 'allergies').filter(is_cured=False)

        medications = []

        for medical_record in medical_records:
            if medical_record.illnesses: medications.append(medical_record.illnesses.medication)
            if medical_record.allergies: medications.append(medical_record.allergies.medication)

        return Response(MedicationSerializer(medications, many=True).data, status=status.HTTP_200_OK)
