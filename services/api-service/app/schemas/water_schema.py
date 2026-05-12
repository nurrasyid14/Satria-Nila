# services/api-service/app/schemas/water_schema.py

from pydantic import BaseModel, Field


class WaterQualityInput(BaseModel):
    """Skema input data sensor kualitas air dari Frontend."""
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
