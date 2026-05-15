# services/api-service/app/routes/predict.py

from fastapi import APIRouter, HTTPException
from ..schemas.water_schema import WaterQualityInput
from ..schemas.prediction_schema import PredictionResponse, TIER_INFO
from ..services.ml_client import call_ml_service
from ..services.data_client import save_to_database

router = APIRouter(prefix="/api/v1/water-quality", tags=["Water Quality"])


@router.post("/predict", response_model=PredictionResponse)
async def predict_and_save(data: WaterQualityInput):
    """
    Endpoint utama yang dipanggil oleh Frontend.
    
    Alur Orkestrasi:
    1. Menerima data sensor dari user/frontend.
    2. Mengirim ke ML-Service untuk prediksi.
    3. Menyimpan data sensor + hasil prediksi ke Data-Service (Supabase).
    4. Mengembalikan respon lengkap (Tier, Deskripsi, Rekomendasi).
    """
    sensor_dict = data.model_dump()

    # --- Langkah 1: Panggil ML-Service ---
    try:
        ml_result = await call_ml_service(sensor_dict)
    except Exception as e:
        raise HTTPException(
            status_code=502,
            detail=f"Gagal menghubungi ML-Service: {str(e)}"
        )

    prediction_tier = ml_result.get("prediction", "Unknown")
    confidence = ml_result.get("confidence", 0.0)

    # --- Langkah 2: Simpan ke Data-Service (Supabase) ---
    try:
        await save_to_database(sensor_dict, prediction_tier)
    except Exception as e:
        # Log error tapi jangan gagalkan seluruh request
        print(f"[WARNING] Gagal menyimpan ke database: {e}")

    # --- Langkah 3: Bangun respon lengkap ---
    tier_detail = TIER_INFO.get(prediction_tier, {
        "description": f"Tier '{prediction_tier}' tidak dikenali.",
        "recommendation": "Silakan hubungi administrator sistem."
    })

    return PredictionResponse(
        prediction_tier=prediction_tier,
        confidence=confidence,
        description=tier_detail["description"],
        recommendation=tier_detail["recommendation"]
    )
