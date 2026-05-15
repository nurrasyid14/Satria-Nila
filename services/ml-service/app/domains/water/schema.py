# services/ml-service/app/domains/water/schema.py
# DOMAIN ENTITY: Definisi kontrak data untuk domain Water Quality

from pydantic import BaseModel, Field


class WaterQualityInput(BaseModel):
    """
    Skema input 14 parameter fisikokimia air.
    Digunakan oleh API Layer untuk validasi request,
    dan oleh Domain Layer untuk inferensi model.
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

    def to_csv_columns(self) -> dict:
        """
        Mapping dari nama field API (snake_case) ke nama kolom CSV
        yang digunakan saat training model PyCaret.
        Ini memastikan inferensi model berjalan benar.
        """
        return {
            "Temperature": self.temperature,
            "Turbidity (cm)": self.turbidity,
            "Dissolved Oxygen (mg/L)": self.dissolved_oxygen,
            "Biochemical Oxygen Demand (mg/L)": self.bod,
            "Carbon Dioxide (CO2)": self.co2,
            "pH": self.ph,
            "Total Alkalinity (mg L-1)": self.alkalinity,
            "Total Hardness (mg L-1)": self.hardness,
            "Calcium (mg L-1)": self.calcium,
            "Ammonia (mg L-1)": self.ammonia,
            "Nitrite (mg L-1)": self.nitrite,
            "Phosphorus (mg L-1)": self.phosphorus,
            "Hydrogen Sulfide (mg L-1)": self.h2s,
            "Plankton Count (No. L-1)": self.plankton_count,
        }
