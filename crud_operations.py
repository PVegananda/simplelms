#!/usr/bin/env python
"""
STEP 3: Query CRUD Operations
Dokumentasi hasil query CRUD dari Django Shell
"""

# ============================================================
# Query 1: CREATE - Buat 2 course baru
# ============================================================

# Cara 1: Menggunakan create()
from courses.models import Course
from django.contrib.auth.models import User

teacher = User.objects.get(username='dosen01')

course_new_1 = Course.objects.create(
    name='Machine Learning',
    description='Belajar machine learning dengan Python',
    price=70000,
    teacher=teacher
)
print(f"Course 1 created: {course_new_1.name} (ID: {course_new_1.id})")

course_new_2 = Course.objects.create(
    name='Cloud Computing',
    description='Belajar cloud computing dengan AWS',
    price=65000,
    teacher=teacher
)
print(f"Course 2 created: {course_new_2.name} (ID: {course_new_2.id})")
