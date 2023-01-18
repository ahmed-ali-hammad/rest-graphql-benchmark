from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

app_name = "patient_info_graphql"

urlpatterns = [
    path('patient/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
