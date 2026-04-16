from django.shortcuts import render
from django.http import JsonResponse
from .models import Course, CourseMember


# Welcome Endpoint
def welcome(request):
    """
    Welcome endpoint - API is running
    """
    return JsonResponse({
        'message': 'Welcome to PasyahDjango API',
        'version': '1.0',
        'endpoints': {
            'health': '/health/',
            'status': '/status/',
            'course_list_baseline': '/lab/course-list/baseline/',
            'course_list_optimized': '/lab/course-list/optimized/',
            'course_members_baseline': '/lab/course-members/baseline/',
            'course_members_optimized': '/lab/course-members/optimized/',
            'course_dashboard_baseline': '/lab/course-dashboard/baseline/',
            'course_dashboard_optimized': '/lab/course-dashboard/optimized/',
        }
    })


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
                'user': member.user_id.username,
                'role': member.roles,
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
        Prefetch('coursemember_set', CourseMember.objects.select_related('user_id'))
    ).all()
    
    data = []
    
    for course in courses:
        members = course.coursemember_set.all()
        member_list = []
        
        for member in members:
            member_list.append({
                'id': member.id,
                'user': member.user_id.username,
                'role': member.roles,
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
        students_count = course.coursemember_set.filter(roles='std').count()
        assistants_count = course.coursemember_set.filter(roles='ast').count()
        
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
        students_count=Count('coursemember', filter=Q(coursemember__roles='std')),
        assistants_count=Count('coursemember', filter=Q(coursemember__roles='ast')),
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


# Health Check Endpoints
def health(request):
    """
    Simple health check endpoint
    """
    try:
        # Check database connection
        Course.objects.count()
        return JsonResponse({
            'status': 'healthy',
            'database': 'connected',
            'message': 'Backend is running successfully'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'unhealthy',
            'database': 'disconnected',
            'error': str(e)
        }, status=500)


def status(request):
    """
    Status endpoint with data summary
    """
    try:
        courses_count = Course.objects.count()
        members_count = CourseMember.objects.count()
        
        return JsonResponse({
            'status': 'ok',
            'environment': 'production' if not __debug__ else 'development',
            'courses': courses_count,
            'members': members_count,
            'message': 'API is operational'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'error': str(e)
        }, status=500)

