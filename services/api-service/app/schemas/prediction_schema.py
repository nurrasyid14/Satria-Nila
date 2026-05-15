# services/api-service/app/schemas/prediction_schema.py
# SCHEMA: Definisi data untuk response prediksi (tanpa logika bisnis)

from pydantic import BaseModel


class PredictionResponse(BaseModel):
    """Skema respon prediksi yang dikirim ke Frontend."""
    prediction_tier: str  # Contoh: "Optimal Suitability", "Reduced Suitability"
    confidence: float
    description: str
    recommendation: str
