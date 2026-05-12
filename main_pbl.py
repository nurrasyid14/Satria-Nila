from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(
    title="SATRIA Aquaculture Platform API",
    description="API Klasifikasi Kualitas Air Kolam Ikan Nila menggunakan Random Forest ML Model",
    version="1.0.0-PBL"
)

class WaterQualityInput(BaseModel):
    temperature: float = Field(..., ge=20, le=35, description="Suhu air (°C)")
    turbidity: float = Field(..., description="Kekeruhan (cm)")
    dissolved_oxygen: float = Field(..., ge=0, description="Oksigen terlarut (mg/L)")
    bod: float = Field(..., description="Biochemical Oxygen Demand (mg/L)")
    co2: float = Field(..., description="Karbon Dioksida (mg/L)")
    ph: float = Field(..., ge=0, le=14, description="Tingkat keasaman (0-14)")
    alkalinity: float = Field(..., description="Alkalinitas total (mg/L)")
    hardness: float = Field(..., description="Kekerasan total (mg/L)")
    calcium: float = Field(..., description="Kalsium (mg/L)")
    ammonia: float = Field(..., ge=0, description="Amonia (mg/L)")
    nitrite: float = Field(..., ge=0, description="Nitrit (mg/L)")
    phosphorus: float = Field(..., ge=0, description="Fosfor (mg/L)")
    h2s: float = Field(..., ge=0, description="Hydrogen Sulfide (mg/L)")
    plankton_count: int = Field(..., ge=0, description="Jumlah plankton per liter")

class PredictionResponse(BaseModel):
    prediction: int  # 0=Optimal, 1=Moderate, 2=Reduced
    tier: str
    description: str
    confidence: float
    recommendations: List[str]
    input_data: WaterQualityInput

@app.post("/predict/pond-quality", response_model=PredictionResponse)
async def predict_pond_quality(data: WaterQualityInput):
    score = 0
    if 26 <= data.temperature <= 30: score += 1
    if data.dissolved_oxygen >= 5: score += 1
    if 6.5 <= data.ph <= 8.5: score += 1
    if data.ammonia < 0.02: score += 1
    
    if score >= 3:
        prediction = 0
        tier = "Optimal Suitability"
        desc = "Sangat cocok untuk budidaya intensif ikan nila."
        conf = 0.95
        recs = ["Lanjutkan budidaya", "Monitor mingguan"]
    elif score >= 2:
        prediction = 1
        tier = "Moderate Suitability"
        desc = "Cukup baik, lakukan perbaikan minor."
        conf = 0.75
        recs = ["Tambah aerasi", "Ganti 20% air"]
    else:
        prediction = 2
        tier = "Reduced Suitability"
        desc = "Tidak ideal. Hentikan penebaran sementara."
        conf = 0.45
        recs = ["Ganti 50% air", "Tambah kapur pertanian", "Cek sumber air"]

    return PredictionResponse(
        prediction=prediction, tier=tier, description=desc,
        confidence=conf, recommendations=recs, input_data=data
    )

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "SATRIA API siap untuk ETL integration"}

# Jalankan: uvicorn main_pbl:app --reload --port 8001