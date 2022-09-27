from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Implementing the swagger docs using drf_yasg lib
schema_view = get_schema_view(
    openapi.Info(
        title="Job Application Review API",
        default_version="v1",
        description="Job Application Review System",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@abc.local"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# Adding app url and static file l.e, resume of the application in the root folder as docs
urlpatterns = [
    path("admin/", admin.site.urls),
    path("job_portal/", include("job_portal.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
