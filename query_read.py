#!/usr/bin/env python
"""
Query 2: READ - Filter course dengan harga > 40000
"""

from courses.models import Course

# Filter courses dengan harga > 40000
expensive_courses = Course.objects.filter(price__gt=40000).order_by('-price')

print("Courses dengan harga > 40000:")
print("=" * 60)
for course in expensive_courses:
    print(f"• {course.name}")
    print(f"  Harga: Rp{course.price:,}")
    print(f"  Teacher: {course.teacher.first_name}")
    print()
