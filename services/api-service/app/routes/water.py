# services/api-service/app/routes/water.py
# APPLICATION LAYER: Endpoint untuk domain Water Quality
# Menggabungkan predict.py dan water.py lama menjadi satu thin controller.

from fastapi import APIRouter, HTTPException
from ..schemas.water_schema import WaterQualityInput
from ..schemas.prediction_schema import PredictionResponse
from ..domain.water_logic import get_tier_recommendation
from ..clients.ml_client import call_ml_service
from ..clients.data_client import save_to_database, get_latest_data

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
        # Log error tapi jangan gagalkan seluruh request (graceful degradation)
        print(f"[WARNING] Gagal menyimpan ke database: {e}")

    # --- Langkah 3: Bangun respon lengkap via Domain Layer ---
    tier_detail = get_tier_recommendation(prediction_tier)

    return PredictionResponse(
        prediction_tier=prediction_tier,
        confidence=confidence,
        description=tier_detail["description"],
        recommendation=tier_detail["recommendation"]
    )


@router.get("/history")
async def get_water_quality_history(limit: int = 10):
    """
    Mengambil riwayat data kualitas air terbaru dari database.
    Endpoint ini meneruskan request ke Data-Service.
    """
    try:
        data = await get_latest_data(limit=limit)
        return {"status": "success", "count": len(data), "data": data}
    except Exception as e:
        raise HTTPException(
            status_code=502,
            detail=f"Gagal mengambil data dari Data-Service: {str(e)}"
        )
