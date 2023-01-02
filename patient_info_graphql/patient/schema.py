from graphene_django import DjangoObjectType
import graphene
from patient.models import Patient

class PatientType(DjangoObjectType):
    class Meta:
        model = Patient
        fields = ("id", "first_name", "last_name", "email", "phone")


class PatientQuery(graphene.ObjectType):
    users = graphene.List(PatientType)

    def resolve_users(root, info):
        return Patient.objects.all()

schema = graphene.Schema(query=PatientQuery)