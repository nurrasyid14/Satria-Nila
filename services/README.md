# Microservices Ecosystem (Phase 1: Water Suitability)

Repositori ini berisi layanan yang membentuk sistem SATRIA Tahap 1, berfokus pada **Water Suitability Assessment** menggunakan snapshot data sensor.

## 🗺️ Peta Layanan

| Service | Port | Tanggung Jawab |
| --- | --- | --- |
| **API-Service** | 8000 | Entry Point, Orkestrasi, Business Logic (Rekomendasi). |
| **ML-Service** | 8001 | Inference Klasifikasi Kualitas Air (Refined Dataset). |
| **Data-Service** | 8002 | Persistence Layer (Supabase Integration). |

## 🔄 Alur Komunikasi (Snapshot Assessment)
1. User menginput **14 parameter** sensor ke Frontend.
2. **API-Service** (:8000) menerima data dan meneruskannya ke **ML-Service** (:8001).
3. **ML-Service** memproses data menggunakan model classifier dan mengembalikan label Tier.
4. **API-Service** menentukan deskripsi & rekomendasi berdasarkan Tier tersebut.
5. **API-Service** memerintahkan **Data-Service** (:8002) untuk menyimpan record ke database.
6. User menerima hasil evaluasi instan beserta panduan mitigasi.

## 🛠️ Persyaratan
- Python 3.10+
- Docker & Docker Compose
- Supabase Project (untuk persistence)
