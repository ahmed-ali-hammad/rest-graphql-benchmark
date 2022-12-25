from django.db import models
from model_utils import TimeStampedModel
from django.utils.translation import gettext_lazy as _


class Patient(TimeStampedModel):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.EmailField(max_length=250)
    phone = models.PositiveBigIntegerField()
    primary_care_physician = models.ForeignKey('Doctor', on_delete=models.PROTECT)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=50)
    weight = models.FloatField()
    height = models.FloatField()
    race = models.CharField(max_length=50)
    is_insured = models.BooleanField(default=False)
    is_smoker = models.BooleanField(default=False)
    is_married = models.BooleanField(default=False)


class EmergencyContact(TimeStampedModel):
    patient = models.OneToOneField(Patient, related_name='emergency_contact', on_delete=models.PROTECT)
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.EmailField(max_length=250)
    phone = models.PositiveBigIntegerField()
    relationship = models.CharField(max_length=250)


class PatientAddress(models.Model):
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
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    phone = models.PositiveBigIntegerField()
    email = models.EmailField(max_length=250)


class Disease(TimeStampedModel):
    disease_name = models.CharField(max_length=225)
    disease_descriptions = models.TextField()
    date_of_discovery = models.DateField()
    patient = models.ManyToManyField(Patient, on_delete=models.SET_NULL)
    cured = models.BooleanField(default=False)


class Medication(TimeStampedModel):
    disease = models.ForeignKey(Disease, on_delete=models.SET_NULL)


