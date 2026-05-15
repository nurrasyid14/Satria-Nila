# services/api-service/app/services/ml_client.py

import httpx
from ..core.config import ML_SERVICE_URL


async def call_ml_service(sensor_data: dict) -> dict:
    """
    Mengirim data sensor ke ML-Service dan menerima hasil prediksi.
    Menggunakan httpx (async) untuk komunikasi antar microservice.
    """
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(
            f"{ML_SERVICE_URL}/predict",
            json=sensor_data
        )
        response.raise_for_status()
        return response.json()
