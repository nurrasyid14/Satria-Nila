# services/data-service/app/routes/water_data.py
# APPLICATION LAYER: Endpoint CRUD untuk data kualitas air
# Logika dari main.py lama dipindahkan ke sini sebagai Thin Controller

from fastapi import APIRouter, HTTPException, Query
from ..core.supabase_client import get_supabase
from ..schemas.water_schema import WaterSampleCreate

router = APIRouter(tags=["Water Data"])


@router.post("/data/samples", status_code=201)
def insert_water_sample(sample: WaterSampleCreate):
    """
    Menyimpan data sensor dan hasil prediksi ke tabel 'water_testing' di Supabase.
    """
    try:
        supabase = get_supabase()
        data_to_insert = sample.model_dump()

        response = supabase.table('water_testing').insert(data_to_insert).execute()

        return {
            "status": "success",
            "message": "Data berhasil disimpan ke database",
            "data": response.data
        }
    except Exception as e:
        error_msg = f"Detail: {str(e)}"
        raise HTTPException(status_code=500, detail=error_msg)


@router.get("/data/samples")
def get_water_samples(
    limit: int = Query(default=10, ge=1, le=100, description="Jumlah data yang diambil"),
    offset: int = Query(default=0, ge=0, description="Offset untuk pagination")
):
    """
    Mengambil daftar riwayat pengukuran kualitas air dengan pagination.
    """
    try:
        supabase = get_supabase()
        response = (
            supabase.table('water_testing')
            .select("*")
            .order("created_at", desc=True)
            .range(offset, offset + limit - 1)
            .execute()
        )
        return {
            "status": "success",
            "count": len(response.data),
            "data": response.data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/data/samples/latest")
def get_latest_samples(limit: int = Query(default=10, ge=1, le=100)):
    """
    Mengambil data riwayat kualitas air terbaru (shortcut tanpa offset).
    """
    try:
        supabase = get_supabase()
        response = (
            supabase.table('water_testing')
            .select("*")
            .order("created_at", desc=True)
            .limit(limit)
            .execute()
        )
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
