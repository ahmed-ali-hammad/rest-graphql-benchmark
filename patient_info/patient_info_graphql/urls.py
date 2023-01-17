from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

app_name = "patient_info_graphql"

urlpatterns = [
    path('patient/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
