from django.shortcuts import render
from django.http import JsonResponse
from .models import Course, CourseMember


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


def course_list_optimized(request):
    """
    Endpoint: /lab/course-list/optimized/
    Optimized: select_related('teacher') = 1 query JOIN
    """
    courses = Course.objects.select_related('teacher').all()
    data = []
    
    for course in courses:
        data.append({
            'id': course.id,
            'name': course.name,
            'teacher': course.teacher.username,
            'price': course.price,
        })
    
    return JsonResponse({'data': data})


def course_members_baseline(request):
    """
    Endpoint: /lab/course-members/baseline/
    N+1 Problem: 1 query courses + N query members per course
    """
    courses = Course.objects.all()
    data = []
    
    for course in courses:
        members = course.coursemember_set.all()
        member_list = []
        
        for member in members:
            member_list.append({
                'id': member.id,
                'user': member.user.username,
                'role': member.role,
            })
        
        data.append({
            'id': course.id,
            'name': course.name,
            'members_count': len(member_list),
            'members': member_list,
        })
    
    return JsonResponse({'data': data})


def course_members_optimized(request):
    """
    Endpoint: /lab/course-members/optimized/
    Optimized: prefetch_related untuk reverse relation
    """
    from django.db.models import Prefetch
    
    courses = Course.objects.prefetch_related(
        Prefetch('coursemember_set', CourseMember.objects.select_related('user'))
    ).all()
    
    data = []
    
    for course in courses:
        members = course.coursemember_set.all()
        member_list = []
        
        for member in members:
            member_list.append({
                'id': member.id,
                'user': member.user.username,
                'role': member.role,
            })
        
        data.append({
            'id': course.id,
            'name': course.name,
            'members_count': len(member_list),
            'members': member_list,
        })
    
    return JsonResponse({'data': data})


def course_dashboard_baseline(request):
    """
    Endpoint: /lab/course-dashboard/baseline/
    Inefficient: Loop untuk count members, banyak query
    """
    courses = Course.objects.all()
    data = []
    
    for course in courses:
        members_count = course.coursemember_set.count()
        students_count = course.coursemember_set.filter(role='std').count()
        assistants_count = course.coursemember_set.filter(role='ast').count()
        
        data.append({
            'id': course.id,
            'name': course.name,
            'teacher': course.teacher.username,
            'total_members': members_count,
            'students': students_count,
            'assistants': assistants_count,
        })
    
    return JsonResponse({'data': data})


def course_dashboard_optimized(request):
    """
    Endpoint: /lab/course-dashboard/optimized/
    Optimized: aggregate di database level + annotate
    """
    from django.db.models import Count, Q
    
    courses = Course.objects.select_related('teacher').annotate(
        total_members=Count('coursemember'),
        students_count=Count('coursemember', filter=Q(coursemember__role='std')),
        assistants_count=Count('coursemember', filter=Q(coursemember__role='ast')),
    ).all()
    
    data = []
    
    for course in courses:
        data.append({
            'id': course.id,
            'name': course.name,
            'teacher': course.teacher.username,
            'total_members': course.total_members,
            'students': course.students_count,
            'assistants': course.assistants_count,
        })
    
    return JsonResponse({'data': data})
