from django.shortcuts import render
from django.http import JsonResponse

# views here.
def studentsView(request):
    students = {'id': 1, 'name': 'Alice', 'age': 20, 'grade': 'A'}
    return JsonResponse(students)