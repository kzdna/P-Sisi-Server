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

## 🚀 Cara Menjalankan Project

### 1. Persiapan Environment
Salin file `.env.example` menjadi `.env` dan sesuaikan konfigurasinya:
```bash
cp .env.example .env