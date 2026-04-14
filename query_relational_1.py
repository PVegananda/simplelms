#!/usr/bin/env python
"""
Query 4.1: Relasional - Tampilkan course beserta nama pengajar
"""

from courses.models import Course

courses = Course.objects.all()

print("Daftar Course dan Pengajar:")
print("=" * 70)
for course in courses:
    print(f"• {course.name}")
    print(f"  Pengajar: {course.teacher.first_name} {course.teacher.last_name}")
    print(f"  Harga: Rp{course.price:,}")
    print()
