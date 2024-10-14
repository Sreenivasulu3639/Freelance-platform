from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),  # List all jobs
    path('create/', views.create_job, name='create_job'),  # Client can post a new job
    path('<int:job_id>/', views.job_detail, name='job_detail'),  # View details of a job
    path('<int:job_id>/bid/', views.bid_on_job, name='bid_on_job'),  # Freelancer can place a bid on a job
]
