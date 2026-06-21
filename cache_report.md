# Cache Report - Redis Implementation

## 📌 Hasil Testing

* First Call: ±2 detik (karena API delay)
* Second Call: <0.1 detik (dari cache)

Hal ini menunjukkan bahwa caching berhasil mengurangi response time secara signifikan.

---

## 💻 Kode Implementasi

Caching dilakukan dengan langkah:

1. Mengecek apakah data tersedia di Redis (GET)
2. Jika ada → langsung return
3. Jika tidak → call API, lalu simpan ke Redis (SETEX)
4. Set expiry selama 300 detik (5 menit)

---

## 🔧 Redis Commands

* `GET weather:Jakarta` → mengambil data cache
* `SETEX weather:Jakarta 300 {...}` → menyimpan cache dengan expiry
* `EXPIRE` → otomatis di-handle oleh SETEX

---

## ❓ Jawaban Pertanyaan

### 1. Kenapa response time berbeda?

Karena pada pemanggilan pertama, data diambil dari API yang lambat (simulasi 2 detik). Sedangkan pada pemanggilan kedua, data diambil dari Redis yang merupakan in-memory storage sehingga jauh lebih cepat.

---

### 2. Apa keuntungan caching?

* Mengurangi response time
* Mengurangi beban API eksternal
* Menghemat resource server
* Meningkatkan performa aplikasi

---

### 3. Kapan sebaiknya tidak menggunakan cache?

* Data sering berubah (real-time data)
* Data sensitif (misalnya token atau password)
* Data harus selalu up-to-date
* Memory terbatas

---

## 📷 Screenshot

(Sisipkan screenshot hasil testing di sini)
