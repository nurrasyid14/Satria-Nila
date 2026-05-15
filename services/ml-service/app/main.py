# services/ml-service/app/main.py
# ENTRY POINT: Inisialisasi FastAPI & pendaftaran router
# File ini sengaja dibuat tipis (thin). Semua logika bisnis ada di domains/.

from fastapi import FastAPI
from .api.router import router as inference_router

app = FastAPI(
    title="SATRIA ML-Service",
    description="Microservice Inference Engine untuk Prediksi Kualitas Air",
    version="2.0.0"
)


@app.get("/health")
def health_check():
    return {"status": "online", "service": "ml-service"}


# Mendaftarkan router dari API Layer
app.include_router(inference_router)
