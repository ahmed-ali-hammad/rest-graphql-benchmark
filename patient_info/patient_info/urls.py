from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("patient_info_graphql/", include("patient_info_graphql.urls", namespace="patient_info_graphql")),
    path("patient_info_restapi/", include("patient_info_restapi.urls", namespace="patient_info_restapi"))
]
