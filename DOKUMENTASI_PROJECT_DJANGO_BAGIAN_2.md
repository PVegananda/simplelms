# DOKUMENTASI LENGKAP PROJECT DJANGO - BAGIAN 2/2

## 10.4 (Lanjutan) Populating Database

```bash
>>> course = Course.objects.get(id=1)
>>> print(course.name)
'Django Advanced'
>>>
>>> # Exit
>>> exit()
```

---

## 11. STUDI KASUS PROJECT

### 11.1 Deskripsi Project Simple LMS

**Simple LMS (Learning Management System)** adalah aplikasi web untuk manajemen pembelajaran online yang memungkinkan:

1. **Pengelolaan Kursus**: Dosen dapat membuat dan mengelola kursus
2. **Pendaftaran Siswa**: Siswa dapat mendaftar dalam kursus
3. **Konten Pembelajaran**: Upload materi dalam bentuk teks, video, dan file
4. **Sistem Komentar**: Diskusi antar siswa dan dosen
5. **Dashboard Analytics**: Visualisasi statistik kursus
6. **Query Optimization Lab**: Demonstrasi optimisasi database

### 11.2 Use Case Diagram

```
┌─────────────────────────────────────────────────────┐
│                   Simple LMS System                 │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌──────────┐                                       │
│  │  Dosen   │──────────────┐                        │
│  └──────────┘              │                        │
│                            │                        │
│  ┌──────────┐              ├──→ Membuat Kursus      │
│  │  Siswa   │──────────────┤    Upload Konten      │
│  └──────────┘              ├──→ Lihat Analytics    │
│                            │    Balas Komentar     │
│  ┌──────────┐              │                        │
│  │ Asisten  │──────────────┤                        │
│  └──────────┘              │                        │
│                            │                        │
│  Admin Panel ◄─────────────┴──────────────────────  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### 11.3 Alur Kerja Aplikasi

#### 11.3.1 Alur User Registration & Course Enrollment

```
Step 1: User Register
────────────────────
→ User input username, email, password
→ Sistem save ke User model
→ User mendapat access token/session

Step 2: User Browse Courses
────────────────────────────
→ User access /lab/course-list/optimized/
→ Backend query database dengan select_related('teacher')
→ Return JSON: [Course 1, Course 2, ...]

Step 3: User Enroll in Course
──────────────────────────────
→ User click "Enroll" button
→ PostRequest ke /api/enroll/
→ Backend create CourseMember record
│  - course_id = Course ID
│  - user_id = User ID
│  - roles = 'std' (student)
→ User sekarang enrolled

Step 4: User Access Course Materials
────────────────────────────────────
→ User access /courses/<id>/materials/
→ Backend query CourseContent parent-less items
→ Return hierarchical structure dengan parent-child relationship
```

#### 11.3.2 Optimisasi Query Flow

```
Timeline Performa:

SEBELUM OPTIMISASI (N+1 Problem):
1. GET /lab/course-list/baseline/ → 11 queries (slow)
   Time: ~500ms
   Response JSON: Courses dengan teacher

SETELAH OPTIMISASI (select_related):
1. GET /lab/course-list/optimized/ → 1 query (fast)
   Time: ~50ms
   Response JSON: Sama, tapi 10x lebih cepat

IMPROVEMENT: 91% query reduction ✅
```

### 11.4 Database Schema

#### 11.4.1 Entity-Relationship Diagram

```
┌─────────────────┐
│     User        │
├─────────────────┤
│ id (PK)         │
│ username        │
│ email           │
│ password        │
└────────┬────────┘
         │ (1)
         │
    ┌────├──────────────────┐
    │    │                  │
  (n)  (n)                (m)
    │    │                  │
    ▼    ▼                  ▼
┌──────────────┐      ┌────────────────────┐
│   Course     │      │   CourseMember     │
├──────────────┤      ├────────────────────┤
│ id (PK)      │◄─────│ id (PK)            │
│ name         │(1)   │ course_id (FK)     │
│ description  │    (n)│ user_id (FK)      │
│ price        │      │ roles              │
│ teacher_id   │      └────────────────────┘
│ (FK to User) │
│ created_at   │         ┌─────────────────────────┐
│ updated_at   │      (n)│   CourseContent         │
└──────────────┘◄────────├─────────────────────────┤
        │          (1)   │ id (PK)                 │
      (1)               │ name                    │
        │               │ description             │
      (n)               │ video_url               │
        │               │ file_attachment         │
        ▼               │ course_id (FK)          │
┌──────────────────┐    │ parent_id (FK to self)  │
│   Comment        │    └─────────────────────────┘
├──────────────────┤
│ id (PK)          │
│ content_id (FK)  │◄────── CourseContent (1)
│ member_id (FK)   │◄────── CourseMember (1)
│ comment (TEXT)   │
│ created_at       │
└──────────────────┘
```

#### 11.4.2 Database Table Structure

**Table: courses_course**
```
Column          | Type        | Constraints
────────────────┼─────────────┼─────────────────
id              | SERIAL      | PRIMARY KEY
name            | VARCHAR(100)| NOT NULL
description     | TEXT        | DEFAULT '-'
price           | INTEGER     | DEFAULT 10000
image           | VARCHAR     | NULL
teacher_id      | INTEGER     | FK→auth_user, RESTRICT
created_at      | TIMESTAMP   | AUTO (NOW)
updated_at      | TIMESTAMP   | AUTO (NOW)
```

**Indexes:**
- `INDEX (price)`
- `INDEX (teacher_id, price)`

---

## 12. KENDALA DAN SOLUSI

### 12.1 Kendala Umum dalam Django Development

#### 12.1.1 N+1 Query Problem

**Gejala:**
- Aplikasi terasa lambat meski data sedikit
- Query yang banyak pada setiap request
- Response time meningkat linear dengan jumlah data

**Diagnosa:**
```python
# Ini menghasilkan N+1 queries:
for course in Course.objects.all():          # Query 1
    print(course.teacher.name)               # Query 2, 3, 4, ...
```

**Solusi:**
```python
# Gunakan select_related untuk ForeignKey
Course.objects.select_related('teacher').all()

# Atau prefetch_related untuk reverse relations
Course.objects.prefetch_related('coursemember_set').all()
```

#### 12.1.2 Migration Conflicts

**Gejala:**
- `"Migration confflicts detected"`
- Multiple migration files dengan same number
- Team collaboration issues

**Penyebab:**
- Multiple developers membuat model changes simultaneously
- Migration files di-merge dengan conflict

**Solusi:**
```bash
# Resolve dengan membuat merge migration
python manage.py makemigrations --merge

# Atau reset migrations (development only):
python manage.py migrate courses zero      # Rollback
rm courses/migrations/0*.py                # Delete migration files
python manage.py makemigrations            # Create fresh
```

#### 12.1.3 Static Files Not Found

**Gejala:**
- CSS/JS tidak loaded di browser
- 404 errors untuk static files

**Penyebab:**
- `DEBUG = False` tapi static files belum di-collect
- `STATIC_ROOT` atau `STATIC_URL` misconfigured

**Solusi:**
```bash
# Collect static files
python manage.py collectstatic --noinput

# Development: Ensure DEBUG=True atau runserver yang auto-serve
DEBUG = True  # In settings.py for development
```

#### 12.1.4 Database Connection Errors

**Gejala:**
```
django.db.utils.OperationalError: could not connect to server: 
Connection refused
```

**Penyebab:**
- Database server tidak running
- Credentials salah
- Host/port wrong

**Solusi:**
```bash
# Check PostgreSQL running
brew services list | grep postgres

# Start PostgreSQL
brew services start postgresql

# Test connection
psql -U lms_user -d lms_db
```

### 12.2 Optimization Tips

#### 12.2.1 Database Query Optimization

**Rule of Thumb:**
- Selalu gunakan `select_related()` untuk ForeignKey
- Selalu gunakan `prefetch_related()` untuk reverse relations
- Gunakan `only()` untuk select specific fields only
- Monitor dengan Django-Silk

**Contoh:**
```python
# Bad
courses = Course.objects.all()

# Good
courses = Course.objects.select_related('teacher').only(
    'id', 'name', 'price', 'teacher__username'
)
```

#### 12.2.2 Async Views (untuk Heavy Processing)

```python
# Jika view sangat slow:
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import asyncio

async def heavy_computation(request):
    # Async operation
    result = await some_async_operation()
    return JsonResponse(result)
```

#### 12.2.3 Caching

```python
from django.views.decorators.cache import cache_page

@cache_page(60 * 5)  # Cache selama 5 menit
def expensive_view(request):
    courses = Course.objects.all()
    return JsonResponse({'courses': courses})
```

### 12.3 Testing

#### 12.3.1 Unit Tests

```python
# courses/tests.py
from django.test import TestCase
from .models import Course
from django.contrib.auth.models import User

class CourseModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('teacher', 'teacher@test.com', 'pass')
    
    def test_course_creation(self):
        course = Course.objects.create(
            name='Python 101',
            description='Learn Python',
            teacher=self.user
        )
        self.assertEqual(course.name, 'Python 101')
        self.assertEqual(course.teacher, self.user)

    def run_tests(self):
        # python manage.py test courses
        pass
```

#### 12.3.2 API Testing

```bash
# Dengan cURL
curl -X GET http://localhost:8000/lab/course-list/optimized/

# Check response status
curl -i http://localhost:8000/health/

# Test dengan JSON data
curl -X POST http://localhost:8000/api/enroll/ \
  -H "Content-Type: application/json" \
  -d '{"course_id": 1, "user_id": 2}'
```

---

## 13. KESIMPULAN

### 13.1 Ringkasan Pembelajaran

Melalui project Simple LMS ini, telah diperoleh pemahaman komprehensif tentang:

#### 13.1.1 Django Framework Fundamentals
✅ Arsitektur MTV dan cara kerjanya
✅ Model design dan relationships
✅ QuerySet API untuk data manipulation
✅ View, template, dan URL routing
✅ Admin interface built-in capabilities

#### 13.1.2 Database Design & Optimization
✅ Relational database concepts
✅ Foreign Keys, reverse relations, self-referencing
✅ N+1 Query Problem identification dan solution
✅ `select_related()`, `prefetch_related()`, `annotate()`
✅ Database profiling dengan Django-Silk
✅ 91% query optimization improvement

#### 13.1.3 Modern Web Development Practices
✅ Containerization dengan Docker
✅ Multi-container orchestration
✅ Environment management
✅ REST API development
✅ JSON serialization

### 13.2 Performance Metrics

**Improvement yang Dicapai:**

| Metric | Baseline | Optimized | Improvement |
|--------|----------|-----------|------------|
| Course List Queries | 11 | 1 | 91% ↓ |
| Course Members Queries | 1 + N + (N*M) | 2 | ~95% ↓ |
| Dashboard Queries | 1 + (3*N) | 2 | ~98% ↓ |
| Response Time | ~500ms | ~50ms | 10x faster |

### 13.3 Key Insights

#### 13.3.1 Importance of Query Optimization
Database query adalah bottleneck yang paling umum dalam web applications. Optimization di level query jauh lebih effective daripada application logic optimization. Django ORM tools (`select_related`, `prefetch_related`, `annotate`) adalah weapon yang very powerful untuk mencapai optimal query execution.

#### 13.3.2 Database Design Matters
Relationship modeling yang tepat (Foreign Key, correct on_delete behavior, strategic indexing) adalah foundation dari scalable application. Poor database design tidak bisa di-fix hanya dengan optimization query.

#### 13.3.3 Profiling is Essential
Tanpa profiling tools, tidak bisa tahu bottleneck mana. Django-Silk memberikan visibility penuh tentang apa yang terjadi di database, sehingga optimization decision bisa data-driven.

#### 13.3.4 Containerization Enables Reproducibility
Docker ensure bahwa environment di local development sama dengan production. Ini mengeliminasi "works on my machine" problem dan membuat debugging lebih mudah.

### 13.4 Future Enhancements

Untuk pengembangan lebih lanjut, dapat ditambahkan:

1. **Authentication & Authorization**
   - JWT tokens untuk stateless auth
   - Role-based access control (RBAC)
   - Permission checking di views

2. **API Enhancement**
   - Django REST Framework untuk robust APIs
   - Pagination untuk large datasets
   - Filtering, sorting, searching capabilities
   - Rate limiting untuk abuse prevention

3. **Advanced Features**
   - Real-time notifications (WebSockets)
   - File upload/download dengan progress tracking
   - Export to PDF functionality
   - Advanced analytics & reporting

4. **DevOps & Deployment**
   - Continuous Integration/Deployment (CI/CD)
   - Load balancing untuk high availability
   - Database replication untuk fault tolerance
   - Monitoring & alerting systems

5. **Frontend Development**
   - React/Vue integration
   - Real-time UI updates dengan WebSockets
   - Mobile app (React Native/Flutter)
   - Progressive Web App (PWA) features

### 13.5 Learning Outcomes

**Skills yang Telah Dikuasai:**

1. **Backend Development**
   - ✅ Django framework mastery
   - ✅ Database design dan modeling
   - ✅ API development
   - ✅ Performance optimization

2. **Database Management**
   - ✅ SQL understanding (via ORM)
   - ✅ Query optimization techniques
   - ✅ Database profiling
   - ✅ Migration management

3. **DevOps/Deployment**
   - ✅ Docker containerization
   - ✅ Docker Compose orchestration
   - ✅ Environment management
   - ✅ Production readiness

4. **Software Engineering**
   - ✅ Code organization dan modularity
   - ✅ Testing methodology
   - ✅ Debugging techniques
   - ✅ Version control (Git)

### 13.6 Saran untuk Pengembangan Lebih Lanjut

1. **Deep Dive into Django REST Framework**
   - Serializers untuk kompleks data
   - Generic views & viewsets
   - Authentication & permissions
   - Throttling & rate limiting

2. **Advanced Database Concepts**
   - Query optimization advanced techniques
   - Database transactions & concurrency
   - Stored procedures & triggers
   - Database clustering & replication

3. **Full-Stack Development**
   - Frontend framework mastery (React/Vue)
   - Real-time WebSocket development
   - GraphQL untuk flexible APIs
   - Microservices architecture

4. **Production Deployment**
   - Kubernetes untuk container orchestration
   - Monitoring & logging (ELK Stack)
   - CI/CD pipelines (GitHub Actions, Jenkins)
   - Security hardening

### 13.7 Kesimpulan Akhir

Project Simple LMS telah berhasil mendemonstrasikan konsep-konsep fundamental dari Django framework modern, dengan fokus khusus pada database optimization dan performance tuning. Melalui praktik hands-on ini, pemahaman tentang bagaimana web applications bekerja di belakang layar telah meningkat signifikan.

Perjalanan belajar tidak berhenti di sini. Industry terus berkembang dengan teknologi baru, pattern baru, dan best practices baru. Attitude learning adalah yang paling penting untuk lanjut berkembang sebagai developer profesional.

---

## REFERENSI

### Official Documentation
- Django Official Docs: https://docs.djangoproject.com/
- PostgreSQL Docs: https://www.postgresql.org/docs/
- Docker Docs: https://docs.docker.com/

### Tools & Libraries
- Django 6.0: https://www.djangoproject.com/
- psycopg2: https://www.psycopg.org/
- django-silk: https://github.com/jazzband/django-silk
- Django-cors-headers: https://github.com/adamchainz/django-cors-headers

### Tutorials & Resources
- Django for Beginners: https://djangoforbeginners.com/
- Real Python Django Tutorial: https://realpython.com/django-setup/
- Two Scoops of Django: https://www.feldroy.com/books/two-scoops-of-django

---

**Dokumentasi ini dibuat untuk keperluan Ujian Tengah Semester (UTS)**

Tanggal: 23 April 2026  
Penulis: Pascalin Vedavendra  
Status: Selesai ✅

---

## LAMPIRAN

### A. File Structure Lengkap

```
simplelms/
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          (Project configuration)
│   ├── urls.py              (Project-level routing)
│   └── wsgi.py
├── courses/
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   └── [migration files]
│   ├── __init__.py
│   ├── admin.py             (Model registration untuk Admin)
│   ├── apps.py              (App configuration)
│   ├── models.py            (Database models)
│   ├── tests.py             (Unit tests)
│   ├── urls.py              (App-level routing)
│   ├── views.py             (View logic)
│   └── templates/
├── manage.py
├── .env                     (Environment variables)
├── requirements.txt         (Python dependencies)
├── Dockerfile               (Docker image definition)
├── docker-compose.yml       (Multi-container configuration)
├── init-db.sql              (Database initialization)
└── [script files dan lainnya]
```

### B. Quick Commands Reference

```bash
# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Database
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# Running
python manage.py runserver
docker-compose up --build

# Testing
python manage.py test
curl http://localhost:8000/lab/course-list/optimized/

# Admin
python manage.py shell
python manage.py changepassword admin
```

---

**END OF DOCUMENTATION**
