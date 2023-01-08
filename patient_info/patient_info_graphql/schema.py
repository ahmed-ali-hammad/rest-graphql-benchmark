import graphene
from graphene_django import DjangoObjectType
from patient_info_graphql.models import Patient


class PatientType(DjangoObjectType):
    class Meta:
        model = Patient
        fields = ("id", "first_name", "last_name", "email", "phone")


class PatientQuery(graphene.ObjectType):
    users = graphene.List(PatientType)

    def resolve_users(root, info):
        return Patient.objects.all()

schema = graphene.Schema(query=PatientQuery)