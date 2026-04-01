# 🚀 Simple LMS Docker Stack

### Django + PostgreSQL menggunakan Docker Compose

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge\&logo=django\&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge\&logo=postgresql\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)

---

## 📚 Tentang Proyek

Project ini merupakan implementasi **Simple LMS (Learning Management System)** berbasis **Django** yang dijalankan menggunakan **Docker Compose** dengan arsitektur multi-container.

Terdiri dari:

* 🌐 Django (Web Application)
* 🗄️ PostgreSQL (Database)

Tujuan utama:

* Memahami konsep containerisasi
* Menghubungkan aplikasi dengan database dalam Docker
* Menggunakan environment configuration
* Menerapkan praktik dasar backend modern

---

## 🧩 Tech Stack

* Docker & Docker Compose
* Django (Python)
* PostgreSQL
* python-dotenv

---

## 🧱 Struktur Project

```bash id="h9k3xz"
simple-lms/
├── docker-compose.yml
├── Dockerfile
├── .env.example
├── requirements.txt
├── manage.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── README.md
```

---

## ⚙️ Setup Environment

Salin file environment:

```bash id="c8v0dn"
cp .env.example .env
```

Lalu sesuaikan konfigurasi di dalam `.env`.

---

## 🐳 Menjalankan Project

### 1. Build & Jalankan Container

```bash id="z5h1xy"
docker-compose up --build
```

---

### 2. Jalankan Migrasi Database (jika diperlukan)

```bash id="e4n2rt"
docker exec -it django_app python manage.py migrate
```

---

### 3. Akses Aplikasi

```id="y6t3gp"
http://localhost:8000
```

---

## 🗄️ Persistence Data

PostgreSQL menggunakan Docker volume:

```yaml id="u2j7ks"
postgres_data:/var/lib/postgresql/data
```

Keuntungan:

* Data tidak hilang saat container restart
* Konsisten untuk development

---

## 🔗 Arsitektur Sistem

```id="r3k9wb"
Browser → Django Container → PostgreSQL Container
```

---

## ⚠️ Catatan Penting

* Service `web` menggunakan `depends_on` untuk memastikan database dijalankan terlebih dahulu
* Delay (`sleep`) digunakan agar PostgreSQL siap sebelum Django melakukan koneksi
* Konfigurasi database menggunakan environment variables

---

## 📸 Screenshot

### 🔹 Django Running

![django](screenshots/django.png)

---

## Jawaban Pertanyaan

### 1. Kenapa perlu volume untuk PostgreSQL?

Agar data tetap tersimpan meskipun container dihentikan atau dihapus.

---

### 2. Apa fungsi depends_on?

Untuk memastikan container database dijalankan sebelum aplikasi.

---

### 3. Bagaimana Django connect ke PostgreSQL?

Menggunakan konfigurasi environment variables yang dibaca di `settings.py`.

---

### 4. Apa keuntungan menggunakan PostgreSQL?

Lebih stabil, scalable, dan cocok untuk aplikasi backend dibanding SQLite.

---

## Status

✔️ Docker Compose berjalan
✔️ Django berjalan di container
✔️ PostgreSQL terhubung
✔️ Migrasi database berhasil
✔️ Aplikasi dapat diakses di browser

---

## Author

**Pasyah Vegananda**
