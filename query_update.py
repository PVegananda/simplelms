#!/usr/bin/env python
"""
Query 3: UPDATE - Update harga course dengan id=1 menjadi 75000
"""

from courses.models import Course

# Ambil course dengan id=1
course = Course.objects.get(pk=1)
print(f"Sebelum update:")
print(f"  Course: {course.name}")
print(f"  Harga lama: Rp{course.price:,}")

# Update harga
course.price = 75000
course.save()

print(f"\nSetelah update:")
print(f"  Course: {course.name}")
print(f"  Harga baru: Rp{course.price:,}")
