from django.urls import path
from . import views

urlpatterns = [
    # API endpoints here
    path('students/', views.studentsView)
]