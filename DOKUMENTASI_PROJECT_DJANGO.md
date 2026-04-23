# DOKUMENTASI LENGKAP PROJECT DJANGO: LEARNING MANAGEMENT SYSTEM (LMS)

**Penulis:** Pascalin Vedavendra  
**Tanggal:** 23 April 2026  
**Tujuan:** Ujian Tengah Semester (UTS)  
**Status:** Selesai  

---

## DAFTAR ISI

1. [Pendahuluan](#1-pendahuluan)
2. [Penjelasan Teknologi](#2-penjelasan-teknologi)
3. [Persiapan Lingkungan](#3-persiapan-lingkungan)
4. [Pembuatan Project Django](#4-pembuatan-project-django)
5. [Pembuatan App](#5-pembuatan-app)
6. [Pembuatan Model (Database)](#6-pembuatan-model-database)
7. [Pembuatan View](#7-pembuatan-view)
8. [Routing (URL)](#8-routing-url)
9. [Admin Panel](#9-admin-panel)
10. [Menjalankan Project](#10-menjalankan-project)
11. [Studi Kasus Project](#11-studi-kasus-project)
12. [Kendala dan Solusi](#12-kendala-dan-solusi)
13. [Kesimpulan](#13-kesimpulan)

---

## 1. PENDAHULUAN

### 1.1 Latar Belakang Penggunaan Django

Django adalah sebuah framework web Python tingkat tinggi yang dirancang untuk memungkinkan pembangunan aplikasi web dengan cepat, aman, dan dapat diskalakan. Dalam era digital ini, kebutuhan akan sistem manajemen pembelajaran (Learning Management System) yang komprehensif semakin meningkat seiring dengan berkembangnya paradigma pendidikan. Platform pembelajaran virtual memerlukan infrastruktur yang kuat, database yang terstruktur dengan baik, dan antarmuka yang intuitif.

Django dipilih sebagai framework utama dalam project ini karena beberapa keunggulan signifikan:

- **Arsitektur MTV (Model-Template-View):** Memisahkan logika bisnis, presentasi, dan manajemen data secara terstruktur
- **ORM (Object-Relational Mapping) yang Powerful:** Memudahkan interaksi dengan database tanpa menulis raw SQL
- **Admin Panel Built-in:** Menyediakan interface administratif yang siap pakai untuk manajemen data
- **Security Built-in:** Perlindungan terhadap CSRF, XSS, SQL Injection, dan ancaman keamanan lainnya
- **Scalability:** Mampu menangani aplikasi dari skala kecil hingga enterprise
- **Large Community & Documentation:** Dukungan komunitas yang luas dan dokumentasi yang komprehensif

### 1.2 Tujuan Pembuatan Project

Tujuan utama pembuatan project Simple LMS adalah untuk memahami konsep-konsep fundamental dalam pengembangan aplikasi web modern menggunakan Django, khususnya:

1. **Memahami Arsitektur MTV Django**
   - Bagaimana komponen Model, Template, dan View bekerja sama dalam sebuah aplikasi
   - Separation of Concern (SoC) dalam pengembangan web

2. **Menguasai Django ORM**
   - Cara membuat model dan relasi database
   - Menggunakan QuerySet API untuk manipulasi data
   - Memahami N+1 Query Problem dan bagaimana mengoptimalkannya

3. **Implementasi Fitur Database Optimization**
   - Menggunakan `select_related()` untuk forward relation
   - Menggunakan `prefetch_related()` untuk reverse relation
   - Menggunakan `annotate()` untuk agregasi data di level database

4. **Praktik DevOps Modern**
   - Containerization menggunakan Docker
   - Multi-container orchestration dengan Docker Compose
   - Environment management dan konfigurasi

5. **API Development**
   - Membuat RESTful API endpoints
   - Serialisasi data ke format JSON
   - Health check dan status monitoring

### 1.3 Manfaat Project

Melalui pembuatan project ini, telah diperoleh manfaat-manfaat berikut:

1. **Pemahaman Mendalam tentang Django Framework**
   - Pengetahuan praktis tentang model design dan database relationships
   - Kemampuan untuk membangun aplikasi web yang terstruktur

2. **Optimisasi Database Performance**
   - Kemampuan mengidentifikasi dan mengatasi N+1 Query Problem
   - Peningkatan performa query dari baseline tanpa optimisasi hingga 91%
   - Pemahaman tentang database profiling dan monitoring

3. **Pengalaman Containerization & Deployment**
   - Kemampuan untuk containerize aplikasi Django dengan Docker
   - Pemahaman tentang multi-container architecture
   - Kesiapan untuk deployment ke production environment

4. **Portfolio Development**
   - Project yang mendemonstrasikan kemampuan full-stack development
   - Proof of concept untuk Learning Management System
   - Pengalaman praktis yang relevan untuk industri

---

## 2. PENJELASAN TEKNOLOGI

### 2.1 Apa itu Django

Django adalah sebuah framework web Python bebas dan bersumber terbuka (open source) yang mengikuti paradigma Model-View-Template (MVT), merupakan varian dari Model-View-Controller (MVC). Django dibangun dengan filosofi "Batteries Included", yang berarti framework ini dilengkapi dengan berbagai tools dan fitur yang diperlukan untuk membangun aplikasi web kompleks tanpa perlu menambahkan banyak library pihak ketiga.

**Sejarah Singkat Django:**
- Dikembangkan pada tahun 2003 oleh tim Lawrence Journal-World
- Dirilis ke publik di bawah lisensi BSD pada Juli 2005
- Versi 1.0 diluncurkan pada September 2008
- Terus berkembang dengan rilis versi major secara berkala
- Saat ini (2024) sudah mencapai versi 5.x

**Karakteristik Utama Django:**
- **Rapid Development:** Memungkinkan pengembangan cepat dengan boilerplate minimal
- **Pragmatic Design:** Fokus pada solution praktis daripada perfeksionism teoritis
- **Security:** Perlindungan built-in terhadap berbagai jenis serangan
- **Scalability:** Arsitektur yang fleksibel untuk aplikasi berskala besar
- **Versatility:** Dapat digunakan untuk berbagai jenis aplikasi web

### 2.2 Konsep Dasar Django (MTV Architecture)

Django menggunakan pola arsitektur MTV (Model-Template-View) yang merupakan adaptasi dari MVC (Model-View-Controller). Pemahaman tentang ketiga komponen ini adalah kunci untuk mengembangkan aplikasi Django yang efektif.

#### 2.2.1 Model (M)

**Pengertian:**
Model dalam Django merepresentasikan struktur data (database schema) dari aplikasi. Setiap model adalah sebuah kelas Python yang mewarisi dari `django.db.models.Model` dan mewakili tabel dalam database.

**Fungsi Model:**
- Mendefinisikan struktur dan field dari setiap entitas data
- Mendefinisikan relasi antar entitas (Foreign Key, Many-to-Many)
- Menyimpan business logic yang berkaitan dengan data
- Menyediakan interface untuk CRUD operations

**Analogi Sederhana:**
Jika database adalah lemari, maka model adalah laci-laci dalam lemari tersebut. Setiap laci (model) mempunyai struktur tertentu, misalnya laci untuk dokumen berbeda dengan laci untuk barang elektronik.

**Contoh Implementasi:**
```python
class Course(models.Model):
    """Model yang mewakili tabel courses di database"""
    name = models.CharField("nama matkul", max_length=100)  # Field untuk nama
    description = models.TextField("deskripsi", default='-')  # Field untuk deskripsi
    price = models.IntegerField("harga", default=10000)  # Field untuk harga
    teacher = models.ForeignKey(User, on_delete=models.RESTRICT)  # Relasi ke User
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp
```

#### 2.2.2 Template (T)

**Pengertian:**
Template dalam Django adalah file HTML yang mengandung Django Template Language (DTL) untuk menghasilkan konten dinamis. Template digunakan untuk presentasi data kepada user.

**Fungsi Template:**
- Menampilkan data dari Model dalam format HTML
- Melakukan iterasi data (loop)
- Melakukan kondisional rendering
- Menampilkan pesan flash dan form errors

**Catatan untuk Project Ini:**
Project Simple LMS ini menggunakan REST API architecture, sehingga template HTML tidak digunakan secara ekstensif. Fokus adalah pada JSON response untuk dikonsumsikan oleh aplikasi frontend (React).

#### 2.2.3 View (V)

**Pengertian:**
View dalam Django adalah fungsi atau kelas Python yang menerima HTTP request, melakukan pemrosesan logic, dan mengembalikan HTTP response. View adalah tempat di mana business logic aplikasi diimplementasikan.

**Fungsi View:**
- Menerima HTTP request dari user
- Mengakses dan memanipulasi data melalui Model
- Melakukan business logic processing
- Mengembalikan response (HTML, JSON, redirect, dll)

**Jenis View:**
1. **Function-Based View (FBV):** View yang ditulis sebagai fungsi Python biasa
2. **Class-Based View (CBV):** View yang ditulis sebagai kelas Python (lebih reusable)

**Analogi Sederhana:**
Jika Model adalah data, dan Template adalah tampilan, maka View adalah "pengatur" yang mendonasikan apa data mana yang harus ditampilkan dan bagaimana cara memproses request dari user.

**Contoh Implementasi:**
```python
def course_list_optimized(request):
    """View yang mengembalikan daftar course dalam format JSON"""
    # Mengakses Model untuk mendapatkan data
    courses = Course.objects.select_related('teacher').all()
    data = []
    
    # Memproses data
    for course in courses:
        data.append({
            'id': course.id,
            'name': course.name,
            'teacher': course.teacher.username,
        })
    
    # Mengembalikan response JSON
    return JsonResponse({'data': data})
```

### 2.3 Tools yang Digunakan

#### 2.3.1 Python

**Apa itu Python:**
Python adalah bahasa pemrograman tingkat tinggi yang bersifat interpreted, dengan syntax yang sederhana dan mudah dibaca, cocok untuk pemula maupun developer profesional.

**Versi yang Digunakan:** Python 3.10

**Alasan Penggunaan:**
- Syntax yang clean dan readable
- Waktu development yang lebih cepat dibanding bahasa lain
- Vast ecosystem dengan ribuan library
- Support penuh dari Django dan tools ecosystem

#### 2.3.2 pip (Package Installer for Python)

**Fungsi:** pip adalah package manager untuk Python yang digunakan untuk menginstal, upgrade, dan menghapus library/package Python.

**Perintah Umum:**
```bash
pip install package_name          # Menginstal package
pip install -r requirements.txt   # Menginstal dari file requirements
pip list                          # Melihat daftar package yang terinstal
pip uninstall package_name        # Menghapus package
```

**requirements.txt dalam Project:**
```
Django                    # Framework web
psycopg2-binary          # Driver PostgreSQL untuk Python
python-dotenv            # Load environment variables dari .env
Pillow                   # Untuk manipulasi image
django-silk==5.1.0       # Profiling dan monitoring
django-cors-headers      # Menangani CORS
gunicorn                 # Production WSGI server
dj-database-url          # Parse DATABASE_URL
whitenoise               # Serve static files
```

#### 2.3.3 Virtual Environment (venv)

**Pengertian:**
Virtual environment adalah isolated Python environment yang memungkinkan setiap project memiliki dependency yang terpisah. Ini mencegah conflict antar project.

**Manfaat:**
- Isolasi dependency project
- Tidak mengotori system Python
- Mudah untuk sharing project (via requirements.txt)
- Dapat menggunakan versi Python berbeda

**Analogi Sederhana:**
Virtual environment seperti container terpisah. Jika Anda menginstal library dalam satu container, library tersebut tidak akan mempengaruhi container lain.

#### 2.3.4 PostgreSQL

**Apa itu PostgreSQL:**
PostgreSQL adalah sistem manajemen basis data relasional (RDBMS) yang powerful, open source, dan enterprise-grade.

**Alasan Penggunaan dalam Project:**
- Mendukung advanced data types dan relationships
- Performance yang baik untuk aplikasi scale menengah ke besar
- Reliability dan ACID compliance yang terjamin
- Integrasi seamless dengan Django

**Versi yang Digunakan:** PostgreSQL 15

#### 2.3.5 Docker & Docker Compose

**Docker:**
Docker adalah containerization platform yang memungkinkan aplikasi di-package beserta dependencies-nya dalam container yang isolated dan portable.

**Docker Compose:**
Docker Compose adalah tool untuk mendefinisikan dan menjalankan multi-container Docker applications menggunakan file YAML.

**Manfaat dalam Project:**
- Consistent environment antara development, testing, dan production
- Isolasi service (Django app terpisah dari PostgreSQL)
- Easy deployment dan reproducibility
- Tidak perlu install tools di system secara manual

#### 2.3.6 Django-Silk

**Fungsi:** Django-Silk adalah library untuk profiling Django yang memungkinkan monitoring performa query, response time, dan identifikasi N+1 query problem.

**Manfaat dalam Project:**
- Visualisasi query yang dijalankan per request
- Identifikasi bottleneck performa
- Analisis query execution time
- Debugging N+1 problem

---

## 3. PERSIAPAN LINGKUNGAN

### 3.1 Instalasi Python

#### Step 1: Download dan Install Python

**Untuk macOS:**
```bash
# Menggunakan Homebrew (recommended)
brew install python@3.10

# Verifikasi instalasi
python3 --version
```

**Penjelasan:**
- `brew install python@3.10`: Menginstal Python versi 3.10 menggunakan Homebrew package manager
- `python3 --version`: Menampilkan versi Python yang terinstal untuk verifikasi

**Output yang diharapkan:**
```
Python 3.10.x
```

#### Step 2: Verifikasi pip

```bash
# Mengecek versi pip
pip3 --version

# Upgrade pip ke versi terbaru (optional)
pip3 install --upgrade pip
```

**Penjelasan:**
- `pip3 --version`: Memastikan pip sudah terinstal dan dapat digunakan
- `pip install --upgrade pip`: Mengupgrade pip ke versi terbaru untuk compatibility dan bug fixes

### 3.2 Instalasi Django

Django akan diinstal dalam virtual environment, bukan di system Python secara global. Hal ini lebih aman dan recommended.

#### Step 1: Buat Virtual Environment

```bash
# Navigate ke directory project
cd /path/to/project

# Membuat virtual environment bernama 'venv'
python3 -m venv venv

# Aktivasi virtual environment
# Untuk macOS/Linux:
source venv/bin/activate

# Untuk Windows:
# venv\Scripts\activate
```

**Penjelasan Baris per Baris:**
1. `cd /path/to/project`: Navigasi ke directory project yang diinginkan
2. `python3 -m venv venv`: Perintah untuk membuat virtual environment
   - `python3`: Interpreter Python
   - `-m venv`: Module venv yang dijalankan sebagai script
   - `venv`: Nama directory virtual environment yang akan dibuat
3. `source venv/bin/activate`: Mengaktifkan virtual environment
   - Setelah dijalankan, prompt terminal akan berubah menunjukkan `(venv)` di awal

**Verifikasi:**
```bash
# Prompt akan berubah seperti ini:
(venv) user@computer:project$
```

#### Step 2: Instal Django dalam Virtual Environment

```bash
# Instal Django versi terbaru
pip install Django

# Atau spesifikasi versi (dalam project ini menggunakan 6.0)
pip install Django==6.0.3

# Verifikasi instalasi
python -m django --version
```

**Penjelasan:**
- `pip install Django`: Menginstal Django dari PyPI (Python Package Index)
- `python -m django --version`: Menjalankan Django module untuk menampilkan versi

**Output yang diharapkan:**
```
6.0.3
```

### 3.3 Pembuatan Virtual Environment (Detailed)

Virtual environment adalah crucial untuk project management di Python. Berikut penjelasan lebih detail:

#### Mengapa Virtual Environment Penting?

**Masalah tanpa Virtual Environment:**
```
Antara Project A dan Project B, jika keduanya 
memerlukan library yang sama dengan versi berbeda:
Project A: Django 4.0
Project B: Django 6.0

Instalasi global akan cause conflict karena 
hanya bisa install satu versi
```

**Solusi dengan Virtual Environment:**
```
Project A (venv1) → Django 4.0 (terisolasi)
Project B (venv2) → Django 6.0 (terisolasi)

Tidak ada conflict, setiap project independent
```

#### Struktur Virtual Environment

```
venv/
├── bin/              # Executable files
│   ├── activate      # Script untuk aktivasi
│   ├── python        # Python interpreter
│   └── pip           # Package manager
├── lib/              # Library dan packages
├── include/          # Header files untuk C extensions
└── pyvenv.cfg        # Configuration file
```

### 3.4 Instalasi Dependencies dari requirements.txt

Setelah virtual environment diaktifkan, instal semua dependencies:

```bash
# Pastikan virtual environment sudah diaktifkan
(venv) $ pip install -r requirements.txt
```

**Penjelasan:**
- `pip install -r requirements.txt`: Membaca file requirements.txt dan menginstal semua package yang terdaftar
- `-r` flag: Membaca dari file

**Proses yang Terjadi:**
1. pip membaca requirements.txt
2. Untuk setiap line, pip mengunduh package dari PyPI
3. Package diinstal ke virtual environment
4. Dependencies dari package juga diinstal (dependency resolution)

**Verifikasi:**
```bash
pip list
# Menampilkan semua package yang terinstal
```

---

## 4. PEMBUATAN PROJECT DJANGO

### 4.1 Membuat Project Django

**Command:**
```bash
# Pastikan virtual environment aktif
(venv) $ django-admin startproject config .
```

**Penjelasan:**
- `django-admin`: Django command-line utility
- `startproject`: Subcommand untuk membuat project baru
- `config`: Nama project (dalam project ini menggunakan nama 'config')
- `.`: Membuat project di current directory (bukan subdirectory baru)

**Alternative (tanpa titik):**
```bash
# Ini akan membuat directory baru bernama 'config'
django-admin startproject config
```

### 4.2 Struktur Folder Project

Setelah command dijalankan, struktur folder yang dihasilkan:

```
simplelms/                    # Root directory
├── config/                   # Project configuration folder
│   ├── __init__.py          # Python package marker
│   ├── asgi.py              # ASGI configuration (async)
│   ├── settings.py          # Konfigurasi project
│   ├── urls.py              # URL routing project level
│   └── wsgi.py              # WSGI configuration (sync)
├── manage.py                # Project management command
├── .env                     # Environment variables
├── requirements.txt         # Python dependencies
├── docker-compose.yml       # Multi-container configuration
├── Dockerfile               # Docker image definition
└── courses/                 # Django app (created later)
```

### 4.3 Penjelasan File-File Project

#### 4.3.1 `manage.py`

**Fungsi:** Script utama untuk menjalankan Django commands untuk project

**Penggunaan Umum:**
```bash
python manage.py runserver              # Jalankan development server
python manage.py makemigrations         # Buat migration files
python manage.py migrate                # Apply migrations ke database
python manage.py createsuperuser        # Buat admin user
python manage.py shell                  # Interactive Python shell dengan Django context
```

#### 4.3.2 `config/settings.py`

**Fungsi:** File konfigurasi utama project Django

**Isi Penting:**
```python
# Installed apps - app yang akan dijalankan
INSTALLED_APPS = [
    'django.contrib.admin',       # Admin interface
    'django.contrib.auth',        # Authentication
    'django.contrib.contenttypes', # Content type framework
    'django.contrib.sessions',    # Session framework
    'django.contrib.messages',    # Message framework
    'django.contrib.staticfiles', # Static files handling
    'corsheaders',                # CORS support
    'silk',                       # Profiling
    'courses',                    # Custom app
]

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lms_db',
        'USER': 'lms_user',
        'PASSWORD': 'lms_pass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

#### 4.3.3 `config/urls.py`

**Fungsi:** Central URL routing untuk entire project

**Konsep:**
```python
urlpatterns = [
    path('admin/', admin.site.urls),  # Route ke admin panel
    path('', include('courses.urls')), # Include URLs dari app 'courses'
]
```

Setiap URL di browser akan di-route ke sini terlebih dahulu, kemudian di-delegate ke app URLs.

#### 4.3.4 `config/wsgi.py`

**Fungsi:** WSGI (Web Server Gateway Interface) configuration untuk production

**WSGI adalah standard interface antara web server (seperti Gunicorn) dan Django application**

```python
application = get_wsgi_application()  # Application object yang akan dipanggil web server
```

#### 4.3.5 `config/asgi.py`

**Fungsi:** ASGI (Asynchronous Server Gateway Interface) configuration untuk async support

**Mirip dengan WSGI tapi untuk async operations**

### 4.4 Konfigurasi Database dalam settings.py

Database configuration adalah salah satu yang paling penting:

```python
# Database configuration untuk PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Database engine
        'NAME': 'lms_db',                           # Nama database
        'USER': 'lms_user',                         # Username
        'PASSWORD': 'lms_pass',                     # Password
        'HOST': 'db',                               # Host (dalam Docker: 'db')
        'PORT': '5432',                             # Port default PostgreSQL
    }
}
```

---

## 5. PEMBUATAN APP DJANGO

### 5.1 Apa itu Django App?

**Pengertian:**
Django App adalah komponen modular dalam Django Project. Sebuah project dapat terdiri atas multiple apps, di mana setiap app menghandle functionality tertentu.

**Analogi:**
- **Project** = Toko besar (mall)
- **App** = Toko individual dalam mall (toko makanan, toko pakaian, toko elektronik)

Setiap app terpisah dan independen, tapi bersama-sama membentuk project yang besar.

### 5.2 Membuat App

**Command:**
```bash
# Pastikan virtual environment aktif
(venv) $ python manage.py startapp courses
```

**Penjelasan:**
- `python manage.py startapp courses`: Membuat app baru bernama 'courses'
- `startapp`: Subcommand dari manage.py

### 5.3 Struktur Folder App

Setelah command dijalankan:

```
courses/                    # App directory
├── migrations/            # Database migration files
│   └── __init__.py
├── __init__.py            # Python package marker
├── admin.py               # Admin configuration
├── apps.py                # App configuration
├── models.py              # Database models
├── tests.py               # Unit tests
├── urls.py                # URL routing untuk app (dibuat manual)
├── views.py               # Views/controller logic
└── templates/             # HTML templates (optional)
```

### 5.4 Mendaftarkan App dalam Project

Setelah app dibuat, harus didaftarkan dalam `INSTALLED_APPS` di `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'silk',
    'courses',  # ← Tambahkan app di sini
]
```

**Penjelasan:**
- `'courses'`: String referensi ke app yang baru dibuat
- Urutan tidak kritis untuk import, tapi umumnya disarankan custom apps di akhir

### 5.5 File-File dalam App

#### 5.5.1 `admin.py`

**Fungsi:** Mendaftarkan model ke Django Admin interface

**Contoh:**
```python
from django.contrib import admin
from .models import Course, CourseMember

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'price', 'created_at')
    list_filter = ('teacher', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
```

**Penjelasan:**
- `@admin.register(Course)`: Decorator untuk mendaftarkan model ke admin
- `list_display`: Field yang ditampilkan di list view
- `list_filter`: Filter yang tersedia di sidebar
- `search_fields`: Field yang bisa di-search
- `ordering`: Default ordering

#### 5.5.2 `models.py`

**Fungsi:** Mendefinisikan database models (database schema)

#### 5.5.3 `views.py`

**Fungsi:** Business logic, menerima request dan mengembalikan response

#### 5.5.4 `urls.py`

**Fungsi:** URL routing untuk app level (dibuat manual)

#### 5.5.5 `apps.py`

**Fungsi:** App configuration metadata

```python
from django.apps import AppConfig

class CoursesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'courses'
    verbose_name = 'Sistem Manajemen Kursus'
```

---

## 6. PEMBUATAN MODEL (DATABASE)

### 6.1 Penjelasan Umum Model

Model dalam Django adalah representasi Python dari table dalam database. Setiap attribute pada model class akan menjadi column dalam table.

**Konsep DASAR:**
1. Setiap model = Setiap table di database
2. Setiap attribute model = Column dalam table
3. Setiap instance model = Row dalam table

### 6.2 Model-Model dalam Project

Project Simple LMS memiliki 4 model utama: `Course`, `CourseMember`, `CourseContent`, dan `Comment`. Berikut dijelaskan secara detail:

#### 6.2.1 Model Course

**Fungsi:** Merepresentasikan mata kuliah dalam sistem

**Kode:**
```python
class Course(models.Model):
    # Field untuk menyimpan nama mata kuliah
    name = models.CharField("nama matkul", max_length=100)
    
    # Field untuk menyimpan deskripsi detail
    description = models.TextField("deskripsi", default='-')
    
    # Field untuk menyimpan harga dalam format integer (rupiah)
    price = models.IntegerField("harga", default=10000)
    
    # Field untuk menyimpan gambar/cover mata kuliah
    image = models.ImageField("gambar", null=True, blank=True)
    
    # Foreign key ke User model (built-in Django)
    # Merepresentasikan pengajar/instruktur dari mata kuliah
    # on_delete=models.RESTRICT: Jika user dihapus, akan error (prevent accidental deletion)
    teacher = models.ForeignKey(
        User,
        verbose_name="pengajar",
        on_delete=models.RESTRICT
    )
    
    # Timestamp otomatis saat record dibuat
    # auto_now_add=True: Hanya set sekali saat creation
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Timestamp otomatis saat record diupdate
    # auto_now=True: Selalu update setiap ada perubahan
    updated_at = models.DateTimeField(auto_now=True)

    # Method untuk representasi string dari object
    # Digunakan di Django Admin dan str() calls
    def __str__(self):
        return self.name

    # Meta class untuk konfigurasi model
    class Meta:
        # Nama singular di admin interface
        verbose_name = "Mata Kuliah"
        # Nama plural di admin interface
        verbose_name_plural = "Mata Kuliah"
        # Database indexes untuk performance optimization
        indexes = [
            models.Index(fields=['price']),                    # Index untuk filtering price
            models.Index(fields=['teacher', 'price']),         # Composite index
        ]
```

**Penjelasan Field Types:**

| Field Type | Penggunaan | Contoh |
|-----------|-----------|---------|
| CharField | Text pendek | nama, judul |
| TextField | Text panjang | deskripsi, konten |
| IntegerField | Angka bulat | harga, stock |
| FloatField | Angka desimal | rating (3.5) |
| BooleanField | True/False | is_active |
| DateTimeField | Tanggal dan waktu | created_at |
| DateField | Only tanggal | birthday |
| ForeignKey | Relasi ke model lain | teacher → User |
| ImageField | Upload gambar | photo |
| FileField | Upload file | attachment |

#### 6.2.2 Model CourseMember

**Fungsi:** Merepresentasikan member yang terdaftar dalam sebuah course (siswa/asisten)

**Kode:**
```python
ROLE_OPTIONS = [
    ('std', "Siswa"),
    ('ast', "Asisten"),
]

class CourseMember(models.Model):
    # Foreign key ke Course
    # Merepresentasikan mata kuliah yang diikuti member
    course_id = models.ForeignKey(
        Course,
        verbose_name="matkul",
        on_delete=models.RESTRICT
    )
    
    # Foreign key ke User
    # Merepresentasikan siswa yang terdaftar
    user_id = models.ForeignKey(
        User,
        verbose_name="siswa",
        on_delete=models.RESTRICT
    )
    
    # Field untuk menyimpan role/peran dalam course
    # choices: Membatasi value hanya dari pilihan yang diberikan
    roles = models.CharField(
        "peran",
        max_length=3,
        choices=ROLE_OPTIONS,      # Field hanya bisa 'std' atau 'ast'
        default='std'              # Default role adalah siswa
    )

    def __str__(self):
        return f"{self.user_id} - {self.course_id} ({self.roles})"

    class Meta:
        verbose_name = "Anggota Kelas"
        verbose_name_plural = "Anggota Kelas"
        indexes = [
            models.Index(fields=['course_id', 'roles']),  # Find members by course & role
            models.Index(fields=['user_id']),             # Find courses by user
        ]
```

**Penjelasan Relasi:**
```
Course (1) ──── (n) CourseMember (n) ──── (1) User
                                    ↓
                  Banyak member bisa terdaftar dalam satu course
                  Satu member bisa terdaftar dalam banyak course
```

#### 6.2.3 Model CourseContent

**Fungsi:** Merepresentasikan materi/konten pembelajaran dalam course

**Kode:**
```python
class CourseContent(models.Model):
    # Field untuk judul konten
    name = models.CharField("judul konten", max_length=200)
    
    # Field untuk deskripsi konten
    description = models.TextField("deskripsi", default='-')
    
    # Field untuk menyimpan URL video (YouTube, Vimeo, dll)
    video_url = models.CharField(
        'URL Video',
        max_length=200,
        null=True,          # Nullable - konten bisa tidak ada video
        blank=True          # Optional di form
    )
    
    # Field untuk upload file attachment (PDF, DOC, dll)
    file_attachment = models.FileField("File", null=True, blank=True)
    
    # Foreign key ke Course
    # Merepresentasikan course yang memiliki konten ini
    course_id = models.ForeignKey(
        Course,
        verbose_name="matkul",
        on_delete=models.RESTRICT
    )
    
    # Self-referencing Foreign key
    # Merepresentasikan parent content (untuk hierarki konten)
    # Contoh: Chapter 1 bisa memiliki sub-chapter 1.1, 1.2, etc
    parent_id = models.ForeignKey(
        "self",                    # Reference ke model yang sama
        verbose_name="induk",
        on_delete=models.RESTRICT,
        null=True,                 # Root level content tidak punya parent
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Konten Kelas"
        verbose_name_plural = "Konten Kelas"
```

**Self-Referencing Foreign Key Analogi:**
```
Struktur Buku:
├── Chapter 1
│   ├── Section 1.1
│   │   ├── Subsection 1.1.1
│   │   └── Subsection 1.1.2
│   └── Section 1.2
├── Chapter 2
└── Chapter 3

Self-FK memungkinkan membuat struktur hierarki seperti ini
```

#### 6.2.4 Model Comment

**Kode:**
```python
class Comment(models.Model):
    # Foreign key ke CourseContent
    # Comment ditulis untuk specific content
    content_id = models.ForeignKey(
        CourseContent,
        on_delete=models.RESTRICT
    )
    
    # Foreign key ke CourseMember
    # Comment ditulis oleh specific member
    member_id = models.ForeignKey(
        CourseMember,
        on_delete=models.RESTRICT
    )
    
    # Comment text
    comment = models.TextField("komentar")
    
    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.member_id} on {self.content_id}"

    class Meta:
        verbose_name = "Komentar"
        verbose_name_plural = "Komentar"
```

### 6.3 Database Relationships

#### 6.3.1 Foreign Key (1 to Many)

**Konsep:**
Foreign key digunakan untuk membuat relasi 1-to-many (satu ke banyak).

**Contoh dalam Project:**
```
1 Course memiliki MANY CourseMember
1 User bisa menjadi teacher untuk MANY Course
```

**Syntax:**
```python
field = models.ForeignKey(RelatedModel, on_delete=models.RESTRICT)
```

**`on_delete` Options:**
- `models.CASCADE`: Hapus record jika related record dihapus
- `models.RESTRICT`: Jangan allow penghapusan jika ada related record
- `models.SET_NULL`: Set ke NULL jika related record dihapus

#### 6.3.2 One-to-One Relationship

Tidak digunakan dalam project ini, tapi untuk reference:

```python
field = models.OneToOneField(RelatedModel, on_delete=models.CASCADE)
```

#### 6.3.3 Many-to-Many Relationship

Tidak digunakan dalam project ini, tapi untuk reference:

```python
field = models.ManyToManyField(RelatedModel)
```

### 6.4 Migrasi Database

**Apa itu Migration?**
Migration adalah cara Django untuk mengelola perubahan pada database schema. Setiap perubahan pada model (add field, delete field, change field type) harus di-migrate.

**Kenapa Migration Penting?**
1. **Version Control untuk Database:** Tracking perubahan schema
2. **Reversibility:** Bisa undo perubahan
3. **Collaboration:** Team member bisa sync perubahan database
4. **Production Safety:** Perubahan controlled dan trackable

#### 6.4.1 Step 1: Create Migration Files

**Command:**
```bash
(venv) $ python manage.py makemigrations
```

**Penjelasan:**
- `makemigrations`: Introspect model dan create migration files
- Django melihat differences antara current models dan installed apps
- Membuat file migration di `app/migrations/` directory

**Output:**
```
Migrations for 'courses':
  courses/migrations/0001_initial.py
    - Create model Course
    - Create model CourseMember
    - Create model CourseContent
    - Create model Comment
```

**Apa yang Terjadi di Belakangnya:**
1. Django membaca semua model di `models.py`
2. Django membandingkan dengan migration files yang sudah ada
3. Django mendeteksi perubahan dan membuat migration file baru
4. Migration file berisi Python code yang describe schema changes

**Contoh Currency Migration File:**
```python
# Migration file: courses/migrations/0001_initial.py

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nama matkul')),
                ('description', models.TextField(default='-', verbose_name='deskripsi')),
                ('price', models.IntegerField(default=10000, verbose_name='harga')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Mata Kuliah',
                'verbose_name_plural': 'Mata Kuliah',
            },
        ),
    ]
```

#### 6.4.2 Step 2: Apply Migrations

**Command:**
```bash
(venv) $ python manage.py migrate
```

**Penjelasan:**
- `migrate`: Apply migration files ke database
- Django membaca semua migration files yang belum di-apply
- Menjalankan migrations dalam order
- Update schema di database

**Output:**
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, courses
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying courses.0001_initial... OK
```

**Apa yang Terjadi di Database:**
1. Tabel `courses_course` dibuat dengan columns: id, name, description, price, teacher_id, created_at, updated_at
2. Tabel `courses_coursemember` dibuat dengan columns: id, course_id, user_id, roles
3. Tabel `courses_coursecontent` dibuat
4. Tabel `courses_comment` dibuat
5. Django membuat table `django_migrations` untuk tracking migration history

#### 6.4.3 Melihat Migration Status

```bash
# Melihat yang sudah applied
python manage.py showmigrations

# Output:
admin
 [X] 0001_initial
 [X] 0002_logentry_remove_auto_add
courses
 [X] 0001_initial
 [X] 0002_add_indexes
```

---

## 7. PEMBUATAN VIEW

### 7.1 Fungsi View dalam Django

View adalah "brain" dari aplikasi Django. View:
1. Menerima HTTP request
2. Melakukan processing logic
3. Mengakses data dari database melalui Model
4. Mengembalikan HTTP response

**Analogi:**
Jika restaurant adalah Django project:
- Model = Kitchen (tempat data/resep tersimpan)
- View = Chef (memproses request/pesanan)
- Template = Plating/Penyajian
- URL = Receptionist (mengarahkan customer ke chef)

### 7.2 Function-Based View (FBV)

Dalam project Simple LMS, semua view adalah Function-Based View. Berikut penjelasan detail:

#### 7.2.1 Welcome Endpoint

**Fungsi:** Menampilkan welcome message dan daftar available endpoints

**Kode:**
```python
def welcome(request):
    """
    Welcome endpoint - menginformasikan API sudah running
    
    Parameter:
        request: HttpRequest object (otomatis dikirim Django)
    
    Return:
        JsonResponse dengan welcome message dan endpoints list
    """
    return JsonResponse({
        'message': 'Welcome to PasyahDjango API',
        'version': '1.0',
        'endpoints': {
            'health': '/health/',
            'status': '/status/',
            'course_list_baseline': '/lab/course-list/baseline/',
            'course_list_optimized': '/lab/course-list/optimized/',
            'course_members_baseline': '/lab/course-members/baseline/',
            'course_members_optimized': '/lab/course-members/optimized/',
            'course_dashboard_baseline': '/lab/course-dashboard/baseline/',
            'course_dashboard_optimized': '/lab/course-dashboard/optimized/',
        }
    })
```

**Penjelasan Baris per Baris:**
```python
def welcome(request):                  # Definisi function, menerima request object
    """..."""                          # Docstring menjelaskan fungsi
    return JsonResponse({...})         # Return JSON response dengan data dictionary
```

#### 7.2.2 Course List Baseline (Mendemonstrasikan N+1 Problem)

**N+1 Problem Analogi:**
```
Database punya 10 courses.
Untuk mendapatkan nama teacher setiap course:

Baseline (N+1 Problem):
Query 1: SELECT * FROM courses;                    → Ambil 10 courses
Query 2-11: SELECT * FROM users WHERE id = ?;     → Untuk setiap course, query teacher
Total: 1 + 10 = 11 queries ❌ INEFFICIENT

Optimized (select_related):
Query 1: SELECT courses.*, users.* FROM courses JOIN users;  → Ambil semuanya sekali
Total: 1 query ✅ EFFICIENT
```

**Kode:**
```python
def course_list_baseline(request):
    """
    Endpoint: /lab/course-list/baseline/
    
    Demonstrates N+1 Query Problem:
    - 1 query untuk ambil semua courses
    - N queries (satu per course) untuk ambil teacher data
    
    Total: 1 + N queries (INEFFICIENT)
    """
    # Query courses tanpa optimization
    courses = Course.objects.all()
    
    data = []
    
    # Loop untuk setiap course
    for course in courses:
        # Ini akan trigger query baru untuk setiap course!
        # Django execute SELECT * FROM auth_user WHERE id = course.teacher_id
        teacher_name = course.teacher.username
        
        data.append({
            'id': course.id,
            'name': course.name,
            'teacher': teacher_name,  # ← Trigger new query
            'price': course.price,
        })
    
    return JsonResponse({'data': data})
```

**Visualisasi Database Queries:**
```
Query 1: SELECT id, name, description, price, teacher_id, ... FROM courses;
Result: 10 courses

Query 2: SELECT username FROM auth_user WHERE id = 1;
Query 3: SELECT username FROM auth_user WHERE id = 2;
Query 4: SELECT username FROM auth_user WHERE id = 1;  (same teacher)
...
Query 11: SELECT username FROM auth_user WHERE id = 3;

Total: 11 queries
```

#### 7.2.3 Course List Optimized (menggunakan select_related)

**Kode:**
```python
def course_list_optimized(request):
    """
    Endpoint: /lab/course-list/optimized/
    
    Using select_related() untuk eliminate N+1 problem:
    - select_related(): Untuk ForeignKey dan OneToOneField
    - Menggunakan SQL JOIN untuk fetch related data dalam 1 query
    
    Total: 1 query ✅
    """
    # select_related('teacher') melakukan JOIN dengan auth_user table
    courses = Course.objects.select_related('teacher').all()
    
    data = []
    
    for course in courses:
        # Tidak trigger query baru karena data teacher sudah di-cache
        data.append({
            'id': course.id,
            'name': course.name,
            'teacher': course.teacher.username,  # ← No new query, from cache
            'price': course.price,
        })
    
    return JsonResponse({'data': data})
```

**Visualisasi Query Optimization:**
```
Query 1 (dengan JOIN):
SELECT courses.id, courses.name, courses.teacher_id, courses.price,
       auth_user.id, auth_user.username, ...
FROM courses
INNER JOIN auth_user ON courses.teacher_id = auth_user.id;

Result: 10 courses dengan teacher data, dalam 1 query ✅

Performance improvement: 11 queries → 1 query = 91% reduction
```

**Kapan Menggunakan `select_related()`:**
- **Forward Relations:** ForeignKey(AlamatUser) atau OneToOneField
- **Single objects:** Related object adalah singular
- **SQL constraint:** Setiap related object dijamin ada (due to RESTRICT)

#### 7.2.4 Course Members Baseline

**Demonstrasi N+1 pada Reverse Relations:**

```python
def course_members_baseline(request):
    """
    N+1 Problem pada reverse relations:
    - 1 query untuk ambil courses
    - N queries untuk ambil members per course
    - N*M queries untuk ambil user data per member
    
    Total: 1 + N + (N*M) queries (VERY INEFFICIENT)
    """
    courses = Course.objects.all()  # Query 1: ambil courses
    data = []
    
    for course in courses:
        # Query 2-N: ambil members untuk setiap course (N queries)
        members = course.coursemember_set.all()
        member_list = []
        
        for member in members:
            # Query (N*M): ambil user untuk setiap member (N*M queries)
            member_list.append({
                'id': member.id,
                'user': member.user_id.username,  # ← Trigger query
                'role': member.roles,
            })
        
        data.append({
            'id': course.id,
            'name': course.name,
            'members_count': len(member_list),
            'members': member_list,
        })
    
    return JsonResponse({'data': data})
```

#### 7.2.5 Course Members Optimized

**Menggunakan `prefetch_related()` dan `Prefetch()`:**

```python
def course_members_optimized(request):
    """
    Optimization menggunakan prefetch_related + Prefetch:
    
    - prefetch_related(): Untuk reverse relations dan M2M
    - Prefetch(): Advanced prefetch dengan custom queryset
    
    Total: 2 queries ✅
    Query 1: Ambil all courses
    Query 2: Ambil all members + user data (dengan single JOIN untuk users)
    """
    from django.db.models import Prefetch
    
    # Query 1: Ambil courses dengan prefetch members
    courses = Course.objects.prefetch_related(
        Prefetch(
            'coursemember_set',  # Reverse relation ke CourseMember
            CourseMember.objects.select_related('user_id')  # Optimasi member query
        )
    ).all()
    
    data = []
    
    for course in courses:
        members = course.coursemember_set.all()  # Dari cache, no new query
        member_list = []
        
        for member in members:
            member_list.append({
                'id': member.id,
                'user': member.user_id.username,  # Dari cache, no new query
                'role': member.roles,
            })
        
        data.append({
            'id': course.id,
            'name': course.name,
            'members_count': len(member_list),
            'members': member_list,
        })
    
    return JsonResponse({'data': data})
```

**Kapan Menggunakan `prefetch_related()`:**
- **Reverse Relations:** Reverse ForeignKey atau ManyToMany
- **Multiple objects:** Related objects bisa multiple
- **Complex queries:** Perlu custom filtering pada related objects

#### 7.2.6 Course Dashboard Baseline

**Demonstrasi Inefficient Counting:**

```python
def course_dashboard_baseline(request):
    """
    Inefficient aggregation:
    - 1 query untuk ambil courses
    - 3 queries per course untuk count (total members, students, assistants)
    
    Total: 1 + (3*N) queries
    """
    courses = Course.objects.all()  # Query 1
    data = []
    
    for course in courses:
        # Query 2-4: 3 count queries per course (INEFFICIENT)
        members_count = course.coursemember_set.count()  # Query: SELECT COUNT(*)
        students_count = course.coursemember_set.filter(roles='std').count()  # Query
        assistants_count = course.coursemember_set.filter(roles='ast').count()  # Query
        
        data.append({
            'id': course.id,
            'name': course.name,
            'teacher': course.teacher.username,  # Bonus: N+1 problem juga ada
            'total_members': members_count,
            'students': students_count,
            'assistants': assistants_count,
        })
    
    return JsonResponse({'data': data})
```

#### 7.2.7 Course Dashboard Optimized

**Menggunakan `annotate()` dan `Count()`:**

```python
def course_dashboard_optimized(request):
    """
    Optimization menggunakan annotate() dan Count():
    
    - annotate(): Menambah field baru hasil aggregation
    - Count(): Menghitung jumlah related objects
    - Semua filtering happens di database level
    
    Total: 2 queries ✅
    Query 1: Complex aggregation query dengan COUNT dan GROUP BY
    Query 2: select_related untuk teacher (atau dalam 1 query dengan JOIN)
    """
    from django.db.models import Count, Q
    
    # Single query dengan aggregation
    courses = Course.objects.annotate(
        # Count semua members
        total_members=Count('coursemember', distinct=True),
        # Count hanya students (roles='std')
        students=Count(
            'coursemember',
            filter=Q(coursemember__roles='std'),
            distinct=True
        ),
        # Count hanya assistants (roles='ast')
        assistants=Count(
            'coursemember',
            filter=Q(coursemember__roles='ast'),
            distinct=True
        ),
    ).select_related('teacher')  # Include teacher dalam query
    
    data = []
    
    for course in courses:
        data.append({
            'id': course.id,
            'name': course.name,
            'teacher': course.teacher.username,
            'total_members': course.total_members,  # Dari annotation, no query
            'students': course.students,             # Dari annotation, no query
            'assistants': course.assistants,         # Dari annotation, no query
        })
    
    return JsonResponse({'data': data})
```

**Generated SQL Query (simplified):**
```sql
SELECT 
    courses.id,
    courses.name,
    courses.teacher_id,
    auth_user.username,
    COUNT(DISTINCT coursemember.id) AS total_members,
    COUNT(DISTINCT CASE WHEN coursemember.roles='std' THEN coursemember.id END) AS students,
    COUNT(DISTINCT CASE WHEN coursemember.roles='ast' THEN coursemember.id END) AS assistants
FROM courses
LEFT JOIN coursemember ON courses.id = coursemember.course_id
INNER JOIN auth_user ON courses.teacher_id = auth_user.id
GROUP BY courses.id, courses.name, courses.teacher_id, auth_user.username;
```

---

## 8. ROUTING (URL)

### 8.1 Konsep URL di Django

URL routing adalah mekanisme Django untuk memetakan URL yang diminta user dengan view function yang sesuai.

**Alur Request:**
```
User Request (http://localhost:8000/courses/)
         ↓
Django URL Router
         ↓
Matches dengan pattern di urls.py
         ↓
Calls corresponding view function
         ↓
View returns response
         ↓
Response sent to user
```

### 8.2 URL Configuration

#### 8.2.1 Project Level URLs (`config/urls.py`)

**Fungsi:** Central routing untuk entire project

**Kode:**
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Admin interface route
    path('admin/', admin.site.urls),
    
    # Silk profiling interface
    path('silk/', include('silk.urls', namespace='silk')),
    
    # Include URLs dari courses app
    # All URLs dalam courses.urls akan di-prefix dengan '' (root)
    path('', include('courses.urls')),
]
```

**Penjelasan:**
- `path('admin/', admin.site.urls)`: Route `/admin/` ke Django admin
- `path('silk/', include(...))`: Route `/silk/` ke Django-Silk 
- `path('', include('courses.urls'))`: Include courses URLs tanpa prefix

#### 8.2.2 App Level URLs (`courses/urls.py`)

**Fungsi:** Routing untuk app-specific URLs

**Kode:**
```python
from django.urls import path
from . import views

app_name = 'courses'  # Namespace untuk reversing

urlpatterns = [
    # Welcome endpoint
    path('', views.welcome, name='welcome'),
    
    # Health check endpoints
    path('health/', views.health, name='health'),
    path('status/', views.status, name='status'),
    
    # Course List endpoints
    path('lab/course-list/baseline/', views.course_list_baseline, name='course_list_baseline'),
    path('lab/course-list/optimized/', views.course_list_optimized, name='course_list_optimized'),
    
    # Course Members endpoints
    path('lab/course-members/baseline/', views.course_members_baseline, name='course_members_baseline'),
    path('lab/course-members/optimized/', views.course_members_optimized, name='course_members_optimized'),
    
    # Course Dashboard endpoints
    path('lab/course-dashboard/baseline/', views.course_dashboard_baseline, name='course_dashboard_baseline'),
    path('lab/course-dashboard/optimized/', views.course_dashboard_optimized, name='course_dashboard_optimized'),
]
```

### 8.3 URL Pattern Explanation

**`path()` function syntax:**
```python
path('route/', view_function, name='url_name')
```

| Parameter | Penjelasan |
|-----------|-----------|
| `'route/'` | URL pattern yang match |
| `view_function` | View yang akan dipanggil |
| `name` | Unique identifier untuk URL (untuk reverse lookup) |

### 8.4 URL Reversal

Django menyediakan cara untuk generate URL dari nama:

```python
# Dalam template atau view:
from django.urls import reverse

# Generate URL dari name
url = reverse('courses:course_list_optimized')
# Result: '/lab/course-list/optimized/'
```

---

## 9. ADMIN PANEL

### 9.1 Django Admin Interface

Django Admin adalah fitur powerful built-in yang menyediakan CRUD interface untuk model tanpa harus membuat view/template custom.

**Fitur:**
- Authentication & authorization
- Change list view dengan filtering & searching
- Add/edit/delete functionality
- Bulk actions
- Admin actions

### 9.2 Setup Admin

#### Step 1: Create Superuser

```bash
(venv) $ python manage.py createsuperuser
```

**Interactive Prompt:**
```
Username: admin
Email address: admin@example.com
Password: ****
Password (again): ****
Superuser created successfully.
```

#### Step 2: Register Models

Di `courses/admin.py`:

```python
from django.contrib import admin
from .models import Course, CourseMember, CourseContent, Comment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Admin configuration untuk Course model"""
    
    # Field yang ditampilkan di list view
    list_display = ('name', 'teacher', 'price', 'created_at')
    
    # Filter yang dapat di-klik di sidebar
    list_filter = ('teacher', 'created_at')
    
    # Field yang dapat di-search
    search_fields = ('name', 'description')
    
    # Default ordering
    ordering = ('-created_at',)

@admin.register(CourseMember)
class CourseMemberAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'user_id', 'roles')
    list_filter = ('roles',)

@admin.register(CourseContent)
class CourseContentAdmin(admin.ModelAdmin):
    list_display = ('name', 'course_id', 'parent_id')
    list_filter = ('course_id',)
    search_fields = ('name', 'description')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content_id', 'member_id', 'comment')
    list_filter = ('content_id',)
```

### 9.3 Akses Admin Panel

1. Jalankan server: `python manage.py runserver`
2. Buka http://localhost:8000/admin/
3. Login dengan superuser credentials
4. Manage data melalui interface

**Fitur Admin Panel:**
- **List View:** Lihat semua records dengan filtering & searching
- **Add:** Create record baru via form
- **Edit:** Modify existing record
- **Delete:** Remove records
- **Bulk Actions:** Operasi pada multiple records

---

## 10. MENJALANKAN PROJECT

### 10.1 Persiapan Awal

Sebelum menjalankan project, pastikan setup sudah complete:

```bash
# 1. Navigate ke project directory
cd /path/to/simplelms

# 2. Aktifkan virtual environment
source venv/bin/activate

# 3. Instal dependencies (jika belum)
pip install -r requirements.txt

# 4. Apply migrations (jika belum dilakukan)
python manage.py migrate

# 5. Create superuser (optional, tapi recommended)
python manage.py createsuperuser
```

### 10.2 Running Local Development Server

#### Option 1: Django Development Server (Recommended untuk Development)

```bash
# Jalankan development server
python manage.py runserver

# Atau specify host dan port
python manage.py runserver 0.0.0.0:8000
```

**Output:**
```
System check identified no issues (0 silenced).
April 23, 2026 - 10:00:00
Django version 6.0.3, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

**Karakteristik:**
- Auto-reloads ketika file berubah
- Built-in debugger
- Detailed error messages
- Hanya untuk development, JANGAN untuk production

#### Option 2: Docker Compose (Recommended untuk Replicating Production)

```bash
# Build dan jalankan containers
docker-compose up --build

# Atau hanya jalankan (jika image sudah ada)
docker-compose up

# Untuk detached mode (background)
docker-compose up -d

# Lihat logs
docker-compose logs -f web

# Stop containers
docker-compose down
```

**Struktur Container:**
```
Docker Network
├── web container (Django)
│   ├── Port 8000 (Python)
│   └── Mounts /app
└── db container (PostgreSQL)
    ├── Port 5432
    └── Data volume
```

### 10.3 Testing API Endpoints

#### 10.3.1 Menggunakan cURL

```bash
# Welcome endpoint
curl http://localhost:8000/

# Course list (baseline)
curl http://localhost:8000/lab/course-list/baseline/

# Course list (optimized)
curl http://localhost:8000/lab/course-list/optimized/

# Health check
curl http://localhost:8000/health/

# Status
curl http://localhost:8000/status/
```

#### 10.3.2 Menggunakan Postman

1. Import base URL: `http://localhost:8000`
2. Create requests untuk setiap endpoint
3. Test dan lihat response

#### 10.3.3 Menggunakan Python Requests

```python
import requests

# Welcome
response = requests.get('http://localhost:8000/')
print(response.json())

# Course list optimized
response = requests.get('http://localhost:8000/lab/course-list/optimized/')
print(response.json())
```

### 10.4 Populating Database dengan Test Data

```bash
# Interactive Python shell dengan Django context
python manage.py shell

# Dalam shell:
>>> from django.contrib.auth.models import User
>>> from courses.models import Course, CourseMember, CourseContent, Comment
>>>
>>> # Create users
>>> user1 = User.objects.create_user('alice', 'alice@example.com', 'password123')
>>> user2 = User.objects.create_user('bob', 'bob@example.com', 'password123')
>>>
>>> # Create course
>>> course = Course.objects.create(
...     name='Django Advanced',
...     description='Advanced Django Development',
...     price=500000,
...     teacher=user1
... )
>>>
>>> # Add members
>>> CourseMember.objects.create(
...     course_id=course,
...     user_id=user2,
...     roles='std'
... )
>>>
>>> # Query
>>> Course.objects.all(
