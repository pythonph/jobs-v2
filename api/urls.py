from django.urls import path
from .views import GetAllJobs

urlpatterns = [
    path('all-jobs/', GetAllJobs.as_view(), name='api_all_jobs'),
] 
