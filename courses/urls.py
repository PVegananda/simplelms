from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    # Welcome Endpoint
    path('', views.welcome, name='welcome'),
    
    # Health Check
    path('health/', views.health, name='health'),
    path('status/', views.status, name='status'),
    
    # Course List
    path('lab/course-list/baseline/', views.course_list_baseline, name='course_list_baseline'),
    path('lab/course-list/optimized/', views.course_list_optimized, name='course_list_optimized'),
    
    # Course Members
    path('lab/course-members/baseline/', views.course_members_baseline, name='course_members_baseline'),
    path('lab/course-members/optimized/', views.course_members_optimized, name='course_members_optimized'),
    
    # Course Dashboard
    path('lab/course-dashboard/baseline/', views.course_dashboard_baseline, name='course_dashboard_baseline'),
    path('lab/course-dashboard/optimized/', views.course_dashboard_optimized, name='course_dashboard_optimized'),
]
