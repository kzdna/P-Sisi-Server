# Simple LMS - Project Foundation

Project ini adalah tahap awal pengembangan Learning Management System (LMS) sederhana yang dibangun menggunakan **Django** dan dikontainerisasi menggunakan **Docker**. Fokus utama pada progress ini adalah pengaturan arsitektur dasar dan koneksi database yang stabil.

## 🎯 Fitur & Cakupan (Progress 1)
- Inisialisasi Project Django dengan struktur folder standar.
- Containerization menggunakan Docker (Dockerfile & Docker Compose).
- Database PostgreSQL yang berjalan di dalam container.
- Manajemen konfigurasi menggunakan environment variables (.env).
- Dokumentasi lengkap hasil eksekusi sistem.

## 🛠️ Persyaratan Sistem
- [Docker Desktop](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## 📸 Dokumentasi Sistem

### 1. Django Welcome Page
Halaman awal yang menandakan Django berhasil berjalan dengan sukses di dalam container Docker.
![Welcome Page](screenshots/Django%20Welcome%20Page.png)

### 2. Login Django Admin
Halaman login menuju area administrasi sistem.
![Login Page](screenshots/Login%20Django.png)

### 3. Dashboard Admin
Halaman dashboard admin sebagai bukti database PostgreSQL sudah terkoneksi dan tabel user berhasil dibuat.
![Admin Dashboard](screenshots/Django%20Admin%20Dashboard.png)

### 4. Log Terminal (Docker Compose)
Status log saat service `web` dan `db` berjalan secara paralel dan berstatus healthy.
![Docker Log](screenshots/Log%20Terminal(Docker%20compose).png)

### 5. Hasil Migrasi Database
Bukti eksekusi perintah migrasi yang berhasil membentuk skema database di PostgreSQL.
![Migration Result](screenshots/Hasil%20Eksekusi%20Migrasi.png)

## 🚀 Cara Menjalankan Project

### 1. Persiapan Environment
Salin file `.env.example` menjadi `.env` dan sesuaikan konfigurasinya:
```bash
cp .env.example .env

Cara Run: docker-compose up -d

Cara Load Data: docker exec -it lms_app python manage.py loaddata initial_data.json

Cara Cek Optimasi: docker exec -it lms_app python demo_optimization.py