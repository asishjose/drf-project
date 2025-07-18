from django.urls import path,include
from . import views
# router class for Viewsets
from rest_framework.routers import DefaultRouter


# # router class for Viewsets
router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employee')

urlpatterns = [
    ## API endpoints here
    # FBV examples in urls
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),


    # CBV examples in urls
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view()),

    # path for Viewsets routers
    path('', include(router.urls)),

    ## paths for Blogs & Comments
    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentsView.as_view()),

    #primary key based paths for Blogs & Comments
    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
]