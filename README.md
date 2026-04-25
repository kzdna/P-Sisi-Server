# Simple LMS - Project Foundation & API Implementation

Project ini adalah pengembangan Learning Management System (LMS) sederhana yang dibangun menggunakan **Django** dan dikontainerisasi menggunakan **Docker**. Fokus utama pada progress ini adalah arsitektur backend, koneksi database, sistem autentikasi JWT, dan dokumentasi API interaktif.

## 🎯 Fitur & Cakupan
- **Containerization:** Berjalan sepenuhnya di atas Docker (PostgreSQL & Django).
- **Custom User Model:** Implementasi Role-based access (Student & Instructor).
- **RESTful API:** CRUD lengkap untuk Course, Lesson, Category, dan Enrollment.
- **JWT Authentication:** Keamanan akses menggunakan JSON Web Token.
- **Auto-Generated Documentation:** Swagger UI untuk pengujian API secara langsung.

## 🛠️ Persyaratan Sistem
- [Docker Desktop](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## 📸 Dokumentasi Sistem

### 1. Django Welcome Page & Admin
Status awal Django dan dashboard admin sebagai bukti database PostgreSQL sudah terkoneksi.
![Welcome Page](screenshots/Django%20Welcome%20Page.png)
![Admin Dashboard](screenshots/Django%20Admin%20Dashboard.png)

### 2. Log Sistem & Migrasi
Service `web` dan `db` berjalan healthy dan skema database berhasil terbentuk.
![Docker Log](screenshots/Log%20Terminal(Docker%20compose).png)
![Migration Result](screenshots/Hasil%20Eksekusi%20Migrasi.png)

### 3. API Documentation (Swagger UI)
Seluruh endpoint API terpetakan secara otomatis dan interaktif.
![Swagger UI](screenshots/Swagger_UI_accessible_api_docs.png)

### 4. Autentikasi & Authorization (JWT)
Proses login untuk mendapatkan access token dan cara penggunaannya di header "Bearer".
![API Login](screenshots/loginAPI.png)
![API Authorize](screenshots/LMS%20API%20Project.png)

### 5. Hasil Eksekusi Endpoint (JSON Response)
Bukti endpoint `/api/courses/` berhasil menarik data dari database dengan status **200 OK**.
![GET Courses Success](screenshots/GET_Courses_200_OK.png)

## 🚀 Cara Menjalankan Project
1. Clone repository ini.
2. Jalankan container:
   ```bash
   docker-compose up -d