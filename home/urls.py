from django.urls import path
from .views import OpenView,ProtectedView,RegisterAPI

urlpatterns = [
    path('open/',OpenView.as_view()),
    path('protected/',ProtectedView.as_view()),
    path('register/',RegisterAPI.as_view(),name='register'),
]