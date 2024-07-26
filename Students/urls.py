# Students/urls.py

from django.urls import path
from .views import StudentView

urlpatterns = [
    path('students/', StudentView.as_view(), name='student-list'),  # For POST request
    path('students/<str:student_id>/', StudentView.as_view(), name='student-detail'),  # For GET, PUT, DELETE requests
]
