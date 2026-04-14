#!/usr/bin/env python
"""
Query 4: DELETE - Hapus course yang harganya < 30000
"""

from courses.models import Course

# Cari course dengan harga < 30000
cheap_courses = Course.objects.filter(price__lt=30000)

print(f"Courses yang akan dihapus (harga < 30000): {cheap_courses.count()}")
for course in cheap_courses:
    print(f"  - {course.name} (Rp{course.price:,})")

# Hapus
if cheap_courses.exists():
    deleted_count, _ = cheap_courses.delete()
    print(f"\n✓ {deleted_count} course berhasil dihapus")
else:
    print("\nTidak ada course dengan harga < 30000")
