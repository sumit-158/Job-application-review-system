from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from .serializers import ApplicantSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from .models import *

# Class for compute an oveview of API
class ApiOveview(APIView):
    def get(self, request):
        api_urls = {
            "List": "/applicant-list/",
            "Detail View": "/applicant-detail/<str:pk>/",
            "Create": "/applicant-create/",
            "Update": "/applicant-update/<str:pk>/",
            "Delete": "/applicant-delete/<str:pk>/",
        }

        return Response(api_urls)


class ApplicantList(ListAPIView):
    """
    class for compute all current applicants in the database,Can filter on firstname and email
    """

    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    filter_backends = [SearchFilter]
    search_fields = ["first_name", "email"]


class ApplicantDetail(APIView):
    """
    Class to compute deatil data of applicants
    """

    def get_object(self, pk):
        """
        getting object and validating
        """
        try:
            return Applicant.objects.get(pk=pk)
        except Applicant.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        applicants = self.get_object(pk)
        serializer = ApplicantSerializer(applicants, many=False)
        return Response(serializer.data)


class CreateApplicant(APIView):
    """
    Class to create applicant using applicant model in database
    """

    def post(self, request):
        serializer = ApplicantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_object(pk):
    """
    Helper function for getting allpicant object(Separation of concerns)
    """
    try:
        return Applicant.objects.get(id=pk)
    except Applicant.DoesNotExist:
        raise Http404


class UpdateApplicant(APIView):
    """
    Class to update specific appilcant data in the database
    """

    def put(self, request, pk):
        applicant = get_object(pk)
        serializer = ApplicantSerializer(
            instance=applicant, data=request.data, many=False
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteApplicant(APIView):
    """
    Class to delete a specific applicants using id
    """

    def delete(
        self,
        request,
        pk,
    ):
        applicant = get_object(pk)
        applicant.delete()
        return Response("Applicant Deleted!", status=status.HTTP_204_NO_CONTENT)
