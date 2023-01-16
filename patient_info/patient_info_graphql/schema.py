import graphene
from graphene_django import DjangoObjectType
from patient_info_graphql.models import (Address, Allergy, Doctor,
                                         EmergencyContact, Illness,
                                         MedicalRecord, Medication, Patient,
                                         Surgery)


class PatientType(DjangoObjectType):
    class Meta:
        model = Patient
        fields = ("id", "first_name", "last_name", "email", "phone")


class EmergencyContactType(DjangoObjectType):
    class Meta:
        model = EmergencyContact
        fields = '__all__'


class AddressType(DjangoObjectType):
    class Meta:
        model = Address
        fields = '__all__'


class DoctorType(DjangoObjectType):
    class Meta:
        model = Doctor
        fields = '__all__'


class IllnessType(DjangoObjectType):
    class Meta:
        model = Illness
        fields = '__all__'


class AllergyType(DjangoObjectType):
    class Meta:
        model = Allergy
        fields = '__all__'


class SurgeryType(DjangoObjectType):
    class Meta:
        model = Surgery
        fields = '__all__'


class MedicalRecordType(DjangoObjectType):
    class Meta:
        model = MedicalRecord
        fields = '__all__'


class MedicationType(DjangoObjectType):
    class Meta:
        model = Medication
        fields = '__all__'


class PatientQuery(graphene.ObjectType):
    get_patient = graphene.Field(PatientType, id=graphene.Int())
    get_patient_emergency_contact = graphene.Field(EmergencyContactType, id=graphene.Int())
    get_patient_address = graphene.Field(AddressType, id=graphene.Int())
    get_patient_associated_doctor = graphene.Field(DoctorType, id=graphene.Int())
    get_patient_medical_records = graphene.List(MedicalRecordType, id=graphene.Int())
    get_patient_medication = graphene.List(MedicationType, id=graphene.Int())

    def resolve_get_patient(root, info, id):
        return Patient.objects.get(id=id)

    def resolve_get_patient_emergency_contact(root, info, id):
        return EmergencyContact.objects.get(patient=id)

    def resolve_get_patient_address(root, info, id):
        return Address.objects.get(patient=id)

    def resolve_get_patient_associated_doctor(root, info, id):
        return Patient.objects.get(id=id).primary_care_physician

    def resolve_get_patient_medical_records(root, info, id):
        return Patient.objects.get(id=id).medical_records.all()

    def resolve_get_patient_medication(root, info, id):
        medical_records = Patient.objects.get(id=id).medical_records.select_related(
            'illnesses', 'allergies').filter(is_cured=False)
        medications = []

        for medical_record in medical_records:
            if medical_record.illnesses: medications.append(medical_record.illnesses.medication)
            if medical_record.allergies: medications.append(medical_record.allergies.medication)

        return medications


schema = graphene.Schema(query=PatientQuery)
