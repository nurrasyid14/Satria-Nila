# services/api-service/app/main.py
# ENTRY POINT: Inisialisasi FastAPI & pendaftaran router
# predict.py sudah digabung ke water.py — hanya 2 router yang didaftarkan.

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import health, water

app = FastAPI(
    title="SATRIA API Gateway",
    description=(
        "Gerbang utama (API Gateway) untuk sistem Early Warning System "
        "kualitas air budidaya ikan nila. Layanan ini mengorkestrasi "
        "ML-Service (prediksi) dan Data-Service (database Supabase)."
    ),
    version="2.0.0"
)

# Mengizinkan Frontend (React) mengakses API ini
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Untuk development. Di production, ganti dengan domain spesifik.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mendaftarkan semua route
app.include_router(health.router)
app.include_router(water.router)
