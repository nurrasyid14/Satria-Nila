# services/api-service/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import health, predict, water

app = FastAPI(
    title="SATRIA API Gateway",
    description=(
        "Gerbang utama (API Gateway) untuk sistem Early Warning System "
        "kualitas air budidaya ikan nila. Layanan ini mengorkestrasi "
        "ML-Service (prediksi) dan Data-Service (database Supabase)."
    ),
    version="1.0.0"
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
app.include_router(predict.router)
app.include_router(water.router)
