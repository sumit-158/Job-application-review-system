from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# Adding all the differnet APIs endpoints
urlpatterns = [
    path("", views.ApiOveview.as_view()),
    path("applicant-list/", views.ApplicantList.as_view()),
    path("applicant-list/<str:pk>/", views.ApplicantDetail.as_view()),
    path("applicant-create/", views.CreateApplicant.as_view()),
    path(
        "applicant-update/<str:pk>/",
        views.UpdateApplicant.as_view(),
    ),
    path(
        "applicant-delete/<str:pk>/",
        views.DeleteApplicant.as_view(),
    ),
]
urlpatterns = format_suffix_patterns(urlpatterns)
