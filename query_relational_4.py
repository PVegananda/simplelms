#!/usr/bin/env python
"""
Query 4.4: Relasional - 3 course dengan member terbanyak
"""

from courses.models import Course
from django.db.models import Count

top_courses = Course.objects.annotate(
    member_count=Count('coursemember')
).order_by('-member_count')[:3]

print("Top 3 Courses dengan Member Terbanyak:")
print("=" * 70)
for i, course in enumerate(top_courses, 1):
    print(f"{i}. {course.name}")
    print(f"   Total members: {course.member_count}")
    print()
