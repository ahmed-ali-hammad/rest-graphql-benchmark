from django.db import models
from model_utils import TimeStampedModel
from django.utils.translation import gettext_lazy as _


class Patient(TimeStampedModel):
    """Stores patient's information"""
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.EmailField(max_length=250)
    phone = models.PositiveBigIntegerField()
    primary_care_physician = models.ForeignKey('Doctor',related_name="patients", on_delete=models.PROTECT)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=50)
    weight = models.FloatField()
    height = models.FloatField()
    race = models.CharField(max_length=50)
    is_insured = models.BooleanField(default=False)
    is_smoker = models.BooleanField(default=False)
    is_married = models.BooleanField(default=False)
    illnesses = models.ManyToManyField("Illness", related_name="patients", on_delete=models.PROTECT)
    allergies = models.ManyToManyField("Allergy", related_name="patients", on_delete=models.PROTECT)
    surgeries = models.OneToOneField("Surgery", related_name="patient", on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('Patient')
        verbose_name_plural = _('Patients')


class EmergencyContact(TimeStampedModel):
    """Stores patient's emergency contact"""
    patient = models.OneToOneField(Patient, related_name='emergency_contact', on_delete=models.PROTECT)
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.EmailField(max_length=250)
    phone = models.PositiveBigIntegerField()
    relationship = models.CharField(max_length=250)

    class Meta:
        verbose_name = _('Emergency Contact')
        verbose_name_plural = _('Emergency Contacts')


class Address(TimeStampedModel):
    """Stores a single address entry"""
    patient = models.OneToOneField(Patient, related_name='address', on_delete=models.PROTECT)
    street_address_1 = models.TextField(_('street address 1'))
    street_address_2 = models.TextField(_('street address 2'), blank=True, null=True)
    city = models.CharField(_('city'), max_length=255)
    state = models.CharField(_('state'), max_length=255)
    zip_code = models.PositiveIntegerField(_('zip code'))

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')


class Doctor(TimeStampedModel):
    """Stores a single address entry"""
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    phone = models.PositiveBigIntegerField()
    email = models.EmailField(max_length=250)
    city = models.CharField(_('city'), max_length=255)
    state = models.CharField(_('state'), max_length=255)
    zip_code = models.PositiveIntegerField(_('zip code'))

    class Meta:
        verbose_name = _('Doctor')
        verbose_name_plural = _('Doctors')


class PatientMedicalHistory(TimeStampedModel):
    """Stores the medical history for a patient"""
    patient = models.OneToOneField(Patient, related_name="patient_medical_history", on_delete=models.SET_NULL)
    date_of_discovery = models.DateField()
    cured = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Patient Medical History')
        verbose_name_plural = _('Patients Medical History')


class Medication(TimeStampedModel):
    """stores information about the treatment for a specific illness"""
    title = models.CharField(max_length=225)
    description = models.TextField()
    side_effect = models.TextField()
    dosage_and_administration = models.TextField()
    warnings = models.TextField()
    contraindications = models.TextField()
    Precautions = models.TextField()
    adverse_reactions = models.TextField()

    class Meta:
        verbose_name = _('Medication')
        verbose_name_plural = _('Medications')


class Illness(TimeStampedModel):
    """stores information about a specific illness"""
    title = models.CharField(max_length=225)
    is_curable = models.BooleanField(default=True)
    vaccine_available = models.BooleanField(default=False)
    symptoms = models.TextField()
    causes = models.TextField()
    prevention = models.TextField()
    medication = models.ForeignKey(Medication, related_name="illness", on_delete=models.PROTECT) 

    class Meta:
        verbose_name = _('Illness')
        verbose_name_plural = _('Illnesses')


class Allergy(TimeStampedModel):
    """stores information about a specific allergy"""
    title = models.CharField(max_length=225)
    description = models.TextField()
    symptoms = models.TextField()
    causes = models.TextField()
    medication = models.ForeignKey(Medication, related_name="allergy", on_delete=models.PROTECT) 

    class Meta:
        verbose_name = _('Allergy')
        verbose_name_plural = _('Allergies')

class Surgery(TimeStampedModel):
    title = models.CharField(max_length=225)
    notes = models.TextField()
    date_of_operation = models.DateTimeField()
    discharge_date = models.DateTimeField()
    surgeon = models.ForeignKey('Doctor', related_name="surgeries", on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('Surgery')
        verbose_name_plural = _('Surgeries')