from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from .model.predict import get_prediction

app = FastAPI(
    title="SATRIA ML-Service",
    description="Microservice Inference Engine untuk Prediksi Kualitas Air menggunakan PyCaret",
    version="1.0.0"
)

# Skema data sesuai dengan atribut sensor Anda
class WaterQualityInput(BaseModel):
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

@app.get("/health")
def health_check():
    return {"status": "online", "service": "ml-service"}

@app.post("/predict")
def predict_water_quality(data: WaterQualityInput):
    try:
        # PENTING: PyCaret sensitif terhadap nama kolom. 
        # Kita harus melakukan mapping dari Pydantic Model ke dictionary 
        # yang bentuk string-nya persis dengan header CSV saat training model.
        input_dict = {
            "Temperature": data.temperature,
            "Turbidity (cm)": data.turbidity,
            "Dissolved Oxygen (mg/L)": data.dissolved_oxygen,
            "Biochemical Oxygen Demand (mg/L)": data.bod,
            "Carbon Dioxide (CO2)": data.co2,
            "pH": data.ph,
            "Total Alkalinity (mg L-1)": data.alkalinity,
            "Total Hardness (mg L-1)": data.hardness,
            "Calcium (mg L-1)": data.calcium,
            "Ammonia (mg L-1)": data.ammonia,
            "Nitrite (mg L-1)": data.nitrite,
            "Phosphorus (mg L-1)": data.phosphorus,
            "Hydrogen Sulfide (mg L-1)": data.h2s,
            "Plankton Count (No. L-1)": data.plankton_count
        }
        
        # Panggil fungsi prediksi
        result = get_prediction(input_dict)
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
