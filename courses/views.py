from django.shortcuts import render
from django.http import JsonResponse
from .models import Course


def course_list_baseline(request):
    """
    Endpoint: /lab/course-list/baseline/
    N+1 Problem: 1 query untuk courses + N query untuk teacher
    """
    courses = Course.objects.all()
    data = []
    
    for course in courses:
        data.append({
            'id': course.id,
            'name': course.name,
            'teacher': course.teacher.username,
            'price': course.price,
        })
    
    return JsonResponse({'data': data})
