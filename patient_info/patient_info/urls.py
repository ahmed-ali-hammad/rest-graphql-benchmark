from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)

urlpatterns = [
    # API documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/docs/', SpectacularRedocView.as_view(url_name='schema'), name='docs'),

    path("admin/", admin.site.urls),
    path("patient_info_graphql/", include("patient_info_graphql.urls", namespace="patient_info_graphql")),
    path("patient_info_restapi/", include("patient_info_restapi.urls", namespace="patient_info_restapi"))
]
