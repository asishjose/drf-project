from django.urls import path
from . import views

urlpatterns = [
    ## API endpoints here
    # FBV examples in urls
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),


    # CBV examples in urls
    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view()),

]