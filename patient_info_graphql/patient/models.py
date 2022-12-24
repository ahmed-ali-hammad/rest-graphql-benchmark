from django.db import models
from model_utils import TimeStampedModel


class Patient(TimeStampedModel):
    patient_name = models.CharField(max_length=225)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=50)
    smoking = models.BooleanField(default=False)
    weight = models.FloatField()
    phone = models.PositiveBigIntegerField()


class Doctor(TimeStampedModel):
    patient = models.ManyToManyField(Patient, on_delete=models.SET_NULL)
    doctor_name = models.CharField(max_length=225)
    date_of_birth = models.DateField()
    phone = models.PositiveBigIntegerField()


class Disease(TimeStampedModel):
    disease_name = models.CharField(max_length=225)
    disease_descriptions = models.TextField()
    date_of_discovery = models.DateField()
    patient = models.ManyToManyField(Patient, on_delete=models.SET_NULL)
    cured = models.BooleanField(default=False)


class Medication(TimeStampedModel):
    disease = models.ForeignKey(Disease, on_delete=models.SET_NULL)