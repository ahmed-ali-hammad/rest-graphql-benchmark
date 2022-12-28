from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField


class Patient(TimeStampedModel):
    """Stores patient's information"""

    male = 1
    female = 2

    GENDER_CHOICES = (
        (male, "Male"),
        (female, "Female"),
    )

    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.EmailField(max_length=250)
    phone = PhoneNumberField()
    primary_care_physician = models.ForeignKey('Doctor', related_name="patients", on_delete=models.PROTECT)
    date_of_birth = models.DateField()
    gender = models.IntegerField(choices=GENDER_CHOICES)
    weight = models.FloatField()
    height = models.FloatField()
    is_insured = models.BooleanField(default=False)
    is_smoker = models.BooleanField(default=False)
    is_married = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Patient')
        verbose_name_plural = _('Patients')


class EmergencyContact(TimeStampedModel):
    """Stores patient's emergency contact"""

    spouse = 1
    parent = 2
    sibling = 3
    relative = 4
    friend = 5

    RELATIONSHIP_CHOICES = (
        (spouse, "SPOUSE"),
        (parent, "PARENT"),
        (sibling, "SIBLING"),
        (relative, "RELATIVE"),
        (friend, "FRIEND"),
    )

    patient = models.OneToOneField(Patient, related_name='emergency_contact', on_delete=models.PROTECT)
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.EmailField(max_length=250)
    phone = PhoneNumberField()
    relationship = models.IntegerField(choices=RELATIONSHIP_CHOICES, max_length=250)

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
    phone = PhoneNumberField()
    email = models.EmailField(max_length=250)
    city = models.CharField(_('city'), max_length=255)
    state = models.CharField(_('state'), max_length=255)
    zip_code = models.PositiveIntegerField(_('zip code'))

    class Meta:
        verbose_name = _('Doctor')
        verbose_name_plural = _('Doctors')


class MedicalHistory(TimeStampedModel):
    """Stores the medical history for a patient"""
    patient = models.ForeignKey(Patient, related_name="medical_histories", on_delete=models.PROTECT)
    illnesses = models.ForeignKey("Illness", related_name="medical_histories", on_delete=models.PROTECT, null=True, blank=True)
    allergies = models.ForeignKey("Allergy", related_name="medical_histories", on_delete=models.PROTECT, null=True, blank=True)
    surgeries = models.OneToOneField("Surgery", related_name="medical_history", on_delete=models.PROTECT, null=True, blank=True)
    date_of_discovery = models.DateField()
    physician_notes = models.TextField(null=True, blank=True)
    is_cured = models.BooleanField(default=False)
    required_surgery = models.BooleanField(default=False)
    surgery_perfomed = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Medical History')
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
    medication = models.ForeignKey(Medication, related_name="related_illnesses", on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('Illness')
        verbose_name_plural = _('Illnesses')


class Allergy(TimeStampedModel):
    """stores information about a specific allergy"""
    title = models.CharField(max_length=225)
    description = models.TextField()
    symptoms = models.TextField()
    causes = models.TextField()
    medication = models.ForeignKey(Medication, related_name="related_allergies", on_delete=models.PROTECT) 

    class Meta:
        verbose_name = _('Allergy')
        verbose_name_plural = _('Allergies')


class Surgery(TimeStampedModel):
    patient = models.ForeignKey(Patient, related_name="surgeries", on_delete=models.PROTECT)
    title = models.CharField(max_length=225)
    notes = models.TextField()
    date_of_operation = models.DateTimeField()
    discharge_date = models.DateTimeField(null=True, blank=True)
    surgeon = models.ForeignKey('Doctor', related_name="surgeries", on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('Surgery')
        verbose_name_plural = _('Surgeries')