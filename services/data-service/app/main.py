# services/data-service/app/main.py
# ENTRY POINT: Inisialisasi FastAPI & pendaftaran router
# File ini sengaja dibuat tipis (thin). Semua logika ada di routes/ dan core/.

from fastapi import FastAPI
from .routes.water_data import router as water_router

app = FastAPI(
    title="SATRIA Data-Service",
    description="Microservice untuk mengelola transaksi database Supabase",
    version="2.0.0"
)


@app.get("/health")
def health_check():
    return {"status": "online", "service": "data-service"}


# Mendaftarkan router dari Application Layer
app.include_router(water_router)
