from django.urls import path
from .views import (
    resume_list, add_skill, add_job_listing, shortlist_jobs,upload_resume,add_skill_success,joblisting_list,shortlist_resumes
)

urlpatterns = [
    path('uploadfiles/',upload_resume,name='upload'),
    path('resumes/', resume_list, name='resume_list'),
    path('add_skill/', add_skill, name='add_skill'),
    path('add_skill_success/', add_skill_success, name='add_skill_success'),
    path('add_job_listing/', add_job_listing, name='add_job_listing'),
    path('job_listing_success/',joblisting_list,name="job_listing_success"),
    path('shortlist_jobs/', shortlist_jobs, name='shortlist_jobs'),
    path('shortlist_resumes/', shortlist_resumes, name='shortlist_resumes'),  # Add this line
]


