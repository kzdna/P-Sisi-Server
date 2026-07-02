# FINAL PROJECT REPORT

## 1. Identitas

| Keterangan | Isi |
|------------|-----|
| **Nama** | Salsa Dharma Arindina |
| **NIM** | A11.2023.15246 |
| **Kelas** | A11.4602 |
| **Repository** | https://github.com/kzdna/P-Sisi-Server.git |

---

# 2. Deskripsi Project

Simple LMS API merupakan aplikasi backend berbasis REST API yang dikembangkan menggunakan **Django REST Framework** sebagai sistem manajemen pembelajaran (*Learning Management System*). Sistem menyediakan layanan autentikasi menggunakan **JSON Web Token (JWT)**, pengelolaan data **Course**, **Lesson**, **Enrollment**, serta **Progress** pembelajaran.

Project ini menggunakan **PostgreSQL** sebagai database utama, **Redis** untuk caching dan rate limiting, **MongoDB** untuk activity logging, serta **Docker Compose** agar seluruh layanan dapat dijalankan secara otomatis dalam satu perintah.

Selain itu, dokumentasi API disediakan menggunakan **Swagger/OpenAPI** sehingga memudahkan proses pengujian seluruh endpoint.

---

# 3. Fitur Dasar yang Sudah Berjalan

Fitur utama yang telah berhasil diimplementasikan antara lain:

- ✅ JWT Authentication
- ✅ Role-Based Authorization (Admin, Instructor, Student)
- ✅ Course API (CRUD)
- ✅ Lesson API (CRUD)
- ✅ Enrollment API (CRUD)
- ✅ Progress API
- ✅ Swagger / OpenAPI Documentation
- ✅ PostgreSQL Database
- ✅ Docker Compose Deployment

---

# 4. Fitur Tambahan yang Dipilih

| No | Fitur | Kategori | Poin | Status |
|----|--------|----------|------|--------|
| 1 | Redis Caching | Performance & API Quality | 12 | ✅ Selesai |
| 2 | Cache Invalidation | Performance & API Quality | 12 | ✅ Selesai |
| 3 | Filtering & Search Course | Performance & API Quality | 12 | ✅ Selesai |
| 4 | MongoDB Activity Logging | Analytics & Activity Tracking | 15 | ✅ Selesai |
| 5 | Rate Limiting menggunakan Redis | Security & Account Management | 10 | ✅ Selesai |

Total implementasi fitur telah memenuhi seluruh komponen wajib serta beberapa fitur tambahan sesuai paket penilaian.

---

# 5. Penjelasan Implementasi

## 5.1 PostgreSQL

Project menggunakan PostgreSQL sebagai database utama yang dijalankan melalui Docker Compose. Seluruh migrasi Django berhasil dijalankan sehingga seluruh tabel dapat dibuat secara otomatis.

---

## 5.2 JWT Authentication

Autentikasi menggunakan package **djangorestframework-simplejwt**.

Endpoint yang digunakan:

```
POST /api/auth/login/
POST /api/auth/refresh/
```

Setelah login berhasil, sistem menghasilkan **Access Token** dan **Refresh Token** yang digunakan untuk mengakses endpoint yang membutuhkan autentikasi.

---

## 5.3 Role-Based Authorization

Project menerapkan tiga role pengguna:

- Admin
- Instructor
- Student

Hak akses setiap role:

| Role | Hak Akses |
|------|-----------|
| Student | Melihat Course, Enrollment Course, Update Progress |
| Instructor | Membuat, mengubah, dan mengelola Course |
| Admin | Menghapus Course dan memiliki hak akses penuh |

Implementasi dilakukan menggunakan custom permission pada Django REST Framework.

---

## 5.4 Redis Cache

Redis digunakan sebagai media caching untuk meningkatkan performa endpoint Course.

Caching diterapkan pada:

- GET Course List
- GET Course Detail

Cache akan dihapus otomatis ketika:

- Create Course
- Update Course
- Delete Course

Selain itu Redis juga digunakan sebagai media penyimpanan counter pada fitur **Rate Limiting**.

---

## 5.5 Filtering dan Search

Endpoint Course mendukung:

- Search berdasarkan judul course
- Search berdasarkan deskripsi
- Filter berdasarkan kategori
- Filter berdasarkan instructor

Implementasi menggunakan **Django Filter Backend** dan **Search Filter**.

---

## 5.6 MongoDB Activity Logging

MongoDB digunakan untuk mencatat seluruh aktivitas request pengguna melalui middleware.

Informasi yang dicatat meliputi:

- Username
- HTTP Method
- URL Path
- Timestamp

Seluruh aktivitas disimpan pada collection:

```
activity_logs
```

---

## 5.7 Swagger/OpenAPI

Dokumentasi API dibuat menggunakan package **drf-spectacular**.

Swagger dapat diakses melalui:

```
http://localhost:8000/api/docs/
```

Swagger digunakan untuk melakukan pengujian seluruh endpoint secara langsung melalui browser.

---

# 6. Cara Menjalankan Project

Clone repository.

```bash
git clone https://github.com/kzdna/P-Sisi-Server.git
```

Masuk ke folder project.

```bash
cd simple-lms
```

Salin file environment.

```bash
cp .env.example .env
```

Build dan jalankan Docker.

```bash
docker compose up --build
```

Jalankan migration.

```bash
docker compose exec web python manage.py migrate
```

Buka Swagger.

```
http://localhost:8000/api/docs/
```

---

# 7. Akun Demo

| Role | Username | Password |
|------|----------|----------|
| Admin | salsa | salsa456 |
| Instructor | instructor_salsa | salsa123 |
| Student | salsa | salsa456 |

> Catatan: Pada implementasi project ini, akun **salsa** memiliki role **student** sekaligus status **superuser** sehingga digunakan sebagai akun admin saat pengujian hak akses administrator.

---

# 8. Endpoint Penting

## Authentication

```
POST /api/auth/login/
POST /api/auth/refresh/
```

## Course

```
GET /api/courses/
POST /api/courses/
GET /api/courses/{id}/
PUT /api/courses/{id}/
PATCH /api/courses/{id}/
DELETE /api/courses/{id}/
```

## Lesson

```
GET /api/lessons/
POST /api/lessons/
PUT /api/lessons/{id}/
PATCH /api/lessons/{id}/
DELETE /api/lessons/{id}/
```

## Enrollment

```
GET /api/enrollments/
POST /api/enrollments/
```

## Progress

```
POST /api/enrollments/{id}/progress/
```

---

# 9. Screenshot / Bukti Pengujian

Seluruh hasil pengujian disimpan pada folder:

```
screenshot_pengujian/
```

Berisi:

- swagger.png
- docker_running.png
- jwt_login.png
- course_api_success.png
- student_login.png
- student_get_course.png
- student_enrollment.png
- student_progress.png
- student_forbidden.png
- postgresql_tables.png
- redis_cache.png
- mongodb_activity_logs.png

---

# 10. Kendala dan Solusi

| Kendala | Solusi |
|----------|--------|
| Docker Desktop mengalami error saat build image | Membersihkan cache menggunakan `docker builder prune -a` kemudian melakukan build ulang. |
| Konfigurasi database masih menggunakan SQLite | Mengubah konfigurasi menggunakan PostgreSQL melalui `dj-database-url` dan file `.env`. |
| Dependency `django-environ` dan `psycopg2` belum tersedia | Menambahkan package pada `requirements.txt` kemudian melakukan rebuild Docker. |
| Swagger belum menampilkan endpoint Lesson | Menambahkan `LessonViewSet` pada router di `courses/urls.py`. |
| JWT Token expired saat pengujian | Melakukan login ulang untuk memperoleh Access Token baru. |
| Redis belum menampilkan cache | Memastikan konfigurasi `REDIS_URL` benar dan melakukan pengujian cache melalui Django Cache Framework. |
| MongoDB belum memiliki collection | Memastikan middleware Activity Logging berjalan dan melakukan request API sehingga collection `activity_logs` dibuat otomatis. |

---

# 11. Kesimpulan

Project **Simple LMS API** berhasil dikembangkan menggunakan **Django REST Framework** dengan memanfaatkan **PostgreSQL** sebagai database utama, **Redis** sebagai cache dan rate limiting, **MongoDB** untuk activity logging, serta **Docker Compose** sebagai media deployment.

Seluruh endpoint utama berhasil diimplementasikan dan didokumentasikan menggunakan **Swagger/OpenAPI**. Sistem autentikasi menggunakan JWT beserta Role-Based Authorization juga telah berjalan dengan baik sehingga hak akses pengguna dapat dibedakan sesuai perannya.

Selain mengimplementasikan fitur dasar LMS, project ini juga menerapkan Redis caching, MongoDB activity logging, filtering, dan Docker Compose sehingga backend menjadi lebih optimal, terdokumentasi, serta mudah untuk di-deploy dan dikembangkan lebih lanjut.

---

# Lampiran

- README.md
- FINAL_PROJECT_REPORT.md
- Dockerfile
- docker-compose.yml
- .env.example
- Postman Collection
- Folder `screenshot_pengujian/`