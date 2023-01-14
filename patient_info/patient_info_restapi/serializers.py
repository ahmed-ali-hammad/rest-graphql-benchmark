from patient_info_graphql.models import (Address, Allergy, Doctor,
                                         EmergencyContact, Illness,
                                         MedicalRecord, Medication, Patient,
                                         Surgery)
from rest_framework import serializers


class VerifyPatientIDSerializer(serializers.Serializer):
    patient_id = serializers.IntegerField(required=True)


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['primary_care_physician'] = DoctorSerializer(instance.primary_care_physician).data
        return response


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class AllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergy
        fields = "__all__"


class EmergencyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyContact
        fields = "__all__"


class IllnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Illness
        fields = "__all__"


class SurgerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Surgery
        fields = "__all__"


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['illnesses'] = IllnessSerializer(instance.illnesses).data
        response['allergies'] = AllergySerializer(instance.allergies).data
        response['surgeries'] = SurgerySerializer(instance.surgeries).data
        return response


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = "__all__"
