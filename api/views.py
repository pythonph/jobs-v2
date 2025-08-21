from rest_framework import generics
from jobs.models import Job
from api.serializers import JobSerializer


class GetAllJobs(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
