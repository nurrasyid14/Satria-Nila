# services/data-service/app/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from .db.supabase_client import supabase

app = FastAPI(
    title="SATRIA Data-Service",
    description="Microservice untuk mengelola transaksi database Supabase",
    version="1.0.0"
)

# Skema data yang akan disimpan ke database
class WaterSampleData(BaseModel):
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
    prediction_tier: str  # Menyimpan hasil dari ML-Service (Optimal/Moderate/Reduced)

@app.get("/health")
def health_check():
    return {"status": "online", "service": "data-service"}

@app.post("/api/v1/data/samples")
def insert_water_sample(sample: WaterSampleData):
    """
    Menyimpan data sensor dan hasil prediksi ke database Supabase.
    """
    try:
        data_to_insert = sample.model_dump()
        
        # PENTING: 'water_testing' adalah nama tabel di Supabase. 
        # Jika tabel Anda namanya berbeda, harap ubah di bawah ini.
        response = supabase.table('water_testing').insert(data_to_insert).execute()
        
        return {
            "status": "success", 
            "message": "Data berhasil disimpan ke database",
            "data": response.data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Gagal menyimpan ke database: {str(e)}")

@app.get("/api/v1/data/samples/latest")
def get_latest_samples(limit: int = 10):
    """
    Mengambil data riwayat kualitas air terbaru.
    """
    try:
        response = supabase.table('water_testing').select("*").order("created_at", desc=True).limit(limit).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
