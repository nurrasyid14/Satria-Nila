# services/api-service/app/schemas/prediction_schema.py

from pydantic import BaseModel
from typing import Optional


class PredictionResponse(BaseModel):
    """Skema respon prediksi yang dikirim ke Frontend."""
    prediction_tier: str  # Contoh: "Optimal Suitability", "Reduced Suitability"
    confidence: float
    description: str
    recommendation: str


# Mapping deskripsi dan rekomendasi berdasarkan tier prediksi
TIER_INFO = {
    "Optimal Suitability": {
        "description": "Kualitas air sangat baik dan ideal untuk budidaya ikan nila.",
        "recommendation": "Pertahankan kondisi saat ini. Lakukan monitoring rutin setiap 6 jam."
    },
    "Moderate Suitability": {
        "description": "Kualitas air cukup baik, namun beberapa parameter perlu perhatian.",
        "recommendation": "Periksa parameter yang mendekati ambang batas. Tingkatkan frekuensi monitoring menjadi setiap 3 jam."
    },
    "Reduced Suitability": {
        "description": "Kualitas air kurang ideal. Terdapat parameter yang melebihi ambang batas aman.",
        "recommendation": "SEGERA lakukan tindakan koreksi. Periksa aerasi, lakukan pergantian air parsial, dan cek sumber kontaminan."
    }
}
