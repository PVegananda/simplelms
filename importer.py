#!/usr/bin/env python
"""
Script untuk mengimpor data dari file CSV ke database Django.

Penggunaan:
    docker exec django_app python importer.py

Script ini akan mengimpor:
    1. Data courses dari fixtures/courses.csv
    2. Data course members dari fixtures/members.csv
"""

import csv
import django
import os
import sys

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from courses.models import Course, CourseMember


def import_users():
    """
    Buat user untuk teacher dan siswa yang dibutuhkan.
    
    Teachers:
        - dosen01, dosen02, dosen03
    
    Students:
        - siswa01 - siswa10
    
    Assistants:
        - asisten01, asisten02
    """
    print("=" * 60)
    print("📝 Import Teachers, Students, dan Assistants")
    print("=" * 60)
    
    teachers = [
        {'username': 'dosen01', 'first_name': 'Budi', 'last_name': 'Santoso'},
        {'username': 'dosen02', 'first_name': 'Siti', 'last_name': 'Nurhaliza'},
        {'username': 'dosen03', 'first_name': 'Ahmad', 'last_name': 'Gunawan'},
    ]
    
    # Create teachers
    for teacher in teachers:
        user, created = User.objects.get_or_create(
            username=teacher['username'],
            defaults={
                'first_name': teacher['first_name'],
                'last_name': teacher['last_name'],
                'email': f"{teacher['username']}@university.edu",
            }
        )
        status = "[✓ CREATED]" if created else "[✓ EXISTS]"
        print(f"{status} Teacher: {user.username} ({user.first_name} {user.last_name})")
    
    # Create students
    students = [
        {'username': f'siswa{str(i).zfill(2)}', 'first_name': f'Mahasiswa {i}'} 
        for i in range(1, 11)
    ]
    for student in students:
        user, created = User.objects.get_or_create(
            username=student['username'],
            defaults={
                'first_name': student['first_name'],
                'email': f"{student['username']}@student.edu",
            }
        )
        status = "[✓ CREATED]" if created else "[✓ EXISTS]"
        print(f"{status} Student: {user.username}")
    
    # Create assistants
    assistants = [
        {'username': 'asisten01', 'first_name': 'Rendra', 'last_name': 'Wijaya'},
        {'username': 'asisten02', 'first_name': 'Dina', 'last_name': 'Kusuma'},
    ]
    for assistant in assistants:
        user, created = User.objects.get_or_create(
            username=assistant['username'],
            defaults={
                'first_name': assistant['first_name'],
                'last_name': assistant['last_name'],
                'email': f"{assistant['username']}@university.edu",
            }
        )
        status = "[✓ CREATED]" if created else "[✓ EXISTS]"
        print(f"{status} Assistant: {user.username} ({user.first_name} {user.last_name})")


def import_courses(csv_file='fixtures/courses.csv'):
    """
    Impor data courses dari file CSV.
    
    Format CSV:
        name, description, price, teacher_username
    """
    print("\n" + "=" * 60)
    print("📚 Import Courses dari CSV")
    print("=" * 60)
    
    if not os.path.exists(csv_file):
        print(f"❌ File tidak ditemukan: {csv_file}")
        return False
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            count_created = 0
            count_exists = 0
            
            for row in reader:
                try:
                    # Get teacher user
                    teacher = User.objects.get(username=row['teacher_username'])
                    
                    # Create or update course
                    course, created = Course.objects.get_or_create(
                        name=row['name'],
                        defaults={
                            'description': row['description'],
                            'price': int(row['price']),
                            'teacher': teacher,
                        }
                    )
                    
                    if created:
                        print(f"[✓ CREATED] Course: {course.name} (Rp{course.price:,}) by {teacher.first_name}")
                        count_created += 1
                    else:
                        print(f"[✓ EXISTS]  Course: {course.name}")
                        count_exists += 1
                        
                except User.DoesNotExist:
                    print(f"❌ ERROR: Teacher '{row['teacher_username']}' tidak ditemukan untuk course '{row['name']}'")
                except Exception as e:
                    print(f"❌ ERROR: {str(e)}")
            
            print(f"\n📊 Summary: {count_created} created, {count_exists} already exists")
            return True
            
    except Exception as e:
        print(f"❌ Error membaca file CSV: {str(e)}")
        return False


def import_members(csv_file='fixtures/members.csv'):
    """
    Impor data course members dari file CSV.
    
    Format CSV:
        course_name, username, roles (std=siswa, ast=asisten)
    """
    print("\n" + "=" * 60)
    print("👥 Import Course Members dari CSV")
    print("=" * 60)
    
    if not os.path.exists(csv_file):
        print(f"❌ File tidak ditemukan: {csv_file}")
        return False
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            count_created = 0
            count_exists = 0
            
            for row in reader:
                try:
                    # Get course and user
                    course = Course.objects.get(name=row['course_name'])
                    user = User.objects.get(username=row['username'])
                    
                    # Map role
                    roles = row['roles']
                    role_label = "Asisten" if roles == 'ast' else "Siswa"
                    
                    # Create or update member
                    member, created = CourseMember.objects.get_or_create(
                        course_id=course,
                        user_id=user,
                        defaults={'roles': roles}
                    )
                    
                    if created:
                        print(f"[✓ CREATED] {user.first_name} ({role_label}) → {course.name}")
                        count_created += 1
                    else:
                        print(f"[✓ EXISTS]  {user.first_name} ({role_label}) → {course.name}")
                        count_exists += 1
                        
                except Course.DoesNotExist:
                    print(f"❌ ERROR: Course '{row['course_name']}' tidak ditemukan")
                except User.DoesNotExist:
                    print(f"❌ ERROR: User '{row['username']}' tidak ditemukan")
                except Exception as e:
                    print(f"❌ ERROR: {str(e)}")
            
            print(f"\n📊 Summary: {count_created} created, {count_exists} already exists")
            return True
            
    except Exception as e:
        print(f"❌ Error membaca file CSV: {str(e)}")
        return False


def main():
    """Main function untuk menjalankan semua import."""
    try:
        print("\n")
        print("┌─────────────────────────────────────────────────────────┐")
        print("│        🚀 DJANGO ORM - Data Import Script 🚀           │")
        print("│              Simple LMS Database Import                 │")
        print("└─────────────────────────────────────────────────────────┘")
        
        # Step 1: Create users
        import_users()
        
        # Step 2: Import courses
        import_courses()
        
        # Step 3: Import members
        import_members()
        
        print("\n" + "=" * 60)
        print("✅ Import data selesai dengan sukses!")
        print("=" * 60)
        print("\n📌 Langkah selanjutnya:")
        print("   1. Akses Django Admin: http://localhost:8000/admin/")
        print("   2. Login dengan akun superuser")
        print("   3. Verifikasi data sudah tersimpan dengan benar")
        print("\n")
        
    except Exception as e:
        print(f"\n❌ Fatal error: {str(e)}")
        sys.exit(1)


if __name__ == '__main__':
    main()
