#!/usr/bin/env python
"""
Query 4.2: Relasional - Tampilkan members di course tertentu
"""

from courses.models import Course, CourseMember

course = Course.objects.get(name='Pemrograman Web')
members = course.coursemember_set.all()

print(f"Members terdaftar di '{course.name}':")
print("=" * 70)
for member in members:
    role = "Asisten" if member.roles == 'ast' else "Siswa"
    print(f"• {member.user_id.first_name} ({role})")

print(f"\nTotal: {members.count()} members")
