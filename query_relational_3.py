#!/usr/bin/env python
"""
Query 4.3: Relasional - Hitung jumlah member per course dengan annotate
"""

from courses.models import Course
from django.db.models import Count

courses = Course.objects.annotate(
    member_count=Count('coursemember')
)

print("Jumlah Member per Course:")
print("=" * 70)
for course in courses:
    print(f"• {course.name}: {course.member_count} members")
