from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def students(request):
    students = [
        {'name': 'Alice', 'age': 20, 'grade': 'A'},
        {'name': 'Bob', 'age': 22, 'grade': 'B'},
    ]
    return HttpResponse(students)