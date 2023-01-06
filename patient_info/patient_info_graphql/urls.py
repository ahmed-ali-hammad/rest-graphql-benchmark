from django.urls import path
from graphene_django.views import GraphQLView

app_name = "patient_info_graphql"

urlpatterns = [
    path('patient/', GraphQLView.as_view(graphiql=True)),
]