# services/data-service/app/schemas/water_schema.py
# DOMAIN ENTITIES: Kontrak data untuk domain Water Quality
# Menggantikan definisi inline WaterSampleData yang sebelumnya ada di main.py

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class WaterSampleCreate(BaseModel):
    """
    Skema input untuk menyimpan data pengukuran + hasil prediksi ke database.
    Digunakan oleh endpoint POST /data/samples.
    """
    temperature: float = Field(..., description="Suhu air (°C)")
    turbidity: float = Field(..., description="Kekeruhan (cm)")
    dissolved_oxygen: float = Field(..., description="Oksigen terlarut (mg/L)")
    bod: float = Field(..., description="Biochemical Oxygen Demand (mg/L)")
    co2: float = Field(..., description="Karbon Dioksida (mg/L)")
    ph: float = Field(..., description="Tingkat keasaman (0-14)")
    alkalinity: float = Field(..., description="Alkalinitas total (mg/L)")
    hardness: float = Field(..., description="Kekerasan total (mg/L)")
    calcium: float = Field(..., description="Kalsium (mg/L)")
    ammonia: float = Field(..., description="Amonia (mg/L)")
    nitrite: float = Field(..., description="Nitrit (mg/L)")
    phosphorus: float = Field(..., description="Fosfor (mg/L)")
    h2s: float = Field(..., description="Hydrogen Sulfide (mg/L)")
    plankton_count: float = Field(..., description="Jumlah plankton per liter")
    prediction_tier: str = Field(..., description="Hasil prediksi dari ML-Service (Optimal/Moderate/Reduced)")


class WaterSampleResponse(BaseModel):
    """
    Skema output yang dikembalikan ke API Gateway.
    Menyertakan field dari database (id, created_at).
    """
    id: Optional[int] = None
    temperature: float
    turbidity: float
    dissolved_oxygen: float
    bod: float
    co2: float
    ph: float
    alkalinity: float
    hardness: float
    calcium: float
    ammonia: float
    nitrite: float
    phosphorus: float
    h2s: float
    plankton_count: float
    prediction_tier: str
    created_at: Optional[datetime] = None
