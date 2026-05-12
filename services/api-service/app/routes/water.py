# services/api-service/app/routes/water.py

from fastapi import APIRouter, HTTPException
from ..services.data_client import get_latest_data

router = APIRouter(prefix="/api/v1/water-quality", tags=["Water Quality"])


@router.get("/history")
async def get_water_quality_history(limit: int = 10):
    """
    Mengambil riwayat data kualitas air terbaru dari database.
    Endpoint ini langsung meneruskan request ke Data-Service.
    """
    try:
        data = await get_latest_data(limit=limit)
        return {"status": "success", "count": len(data), "data": data}
    except Exception as e:
        raise HTTPException(
            status_code=502,
            detail=f"Gagal mengambil data dari Data-Service: {str(e)}"
        )
