# SATRIA Data-Service (Persistence Layer)

Data-Service adalah jembatan antara sistem SATRIA dengan database eksternal (**Supabase**).

## 🗄️ Database
- **Provider**: Supabase (PostgreSQL).
- **Table**: `water_testing`.

## ⚙️ Konfigurasi Supabase
Service ini membutuhkan koneksi ke Supabase via `.env`:
```env
SUPABASE_URL=https://xyz.supabase.co (Tanpa /rest/v1/)
SUPABASE_KEY=your-anon-key
```
*Catatan: Pastikan menggunakan `SUPABASE_URL` base saja karena library otomatis menambahkan path REST.*

## 💻 Cara Menjalankan
```bash
uvicorn app.main:app --reload --port 8002
```
Akses dokumentasi API di: `http://127.0.0.1:8002/docs`

## 🛡️ Keamanan & Validasi
- Menggunakan Pydantic untuk validasi data sebelum dikirim ke database.
- Logika koneksi dipusatkan di `app/core/supabase_client.py`.
