# SATRIA API-Service (Gateway & Orchestrator)

API-Service adalah **Main Entry Point** dan **Orchestrator** untuk sistem SATRIA. Service ini bertanggung jawab untuk menerima request dari frontend, melakukan koordinasi dengan ML-Service untuk mendapatkan prediksi, dan menyimpan hasilnya ke Data-Service.

## 🚀 Fitur Utama
- **Orchestrated Workflow**: Menggabungkan proses input sensor, prediksi ML, dan penyimpanan DB dalam satu request.
- **Domain Logic**: Implementasi penentuan Tier Kualitas Air dan pemberian rekomendasi tindakan berdasarkan hasil ML.
- **Actionable Results**: Mengembalikan payload lengkap (`prediction_tier`, `confidence`, `description`, `recommendation`) sesuai PRD F4 untuk kebutuhan rendering UI Card.
- **Graceful Degradation**: Jika penyimpanan ke database gagal, API tetap akan mengembalikan hasil prediksi ke user.

## 🏗️ Arsitektur (Fundamental DDD)
Service ini mengikuti prinsip *Layered Architecture*:
- **Routes (`app/routes/`)**: Layer aplikasi yang menangani HTTP request/response.
- **Domain (`app/domain/`)**: Layer bisnis yang berisi logika `water_logic.py` (TIER_INFO & Rekomendasi).
- **Clients (`app/clients/`)**: Layer infrastruktur yang menangani komunikasi HTTP ke microservices lain (ML & Data).

## 🛠️ Konfigurasi Environment
Pastikan file `.env` di root project memiliki variabel berikut:
```env
ML_SERVICE_URL=http://127.0.0.1:8001
DATA_SERVICE_URL=http://127.0.0.1:8002
```

## 💻 Cara Menjalankan
```bash
uvicorn app.main:app --reload --port 8000
```
Akses dokumentasi API di: `http://127.0.0.1:8000/docs`
