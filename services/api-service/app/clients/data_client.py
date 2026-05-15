# services/api-service/app/clients/data_client.py
# INFRASTRUCTURE: Client untuk komunikasi dengan Data-Service (Supabase)

import httpx
from ..core.config import DATA_SERVICE_URL


async def save_to_database(sensor_data: dict, prediction_tier: str) -> dict:
    """
    Mengirim data sensor + hasil prediksi ke Data-Service untuk disimpan ke Supabase.
    """
    # Gabungkan data sensor dengan hasil prediksi
    payload = {**sensor_data, "prediction_tier": prediction_tier}

    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(
            f"{DATA_SERVICE_URL}/data/samples",
            json=payload
        )
        response.raise_for_status()
        return response.json()


async def get_latest_data(limit: int = 10) -> list:
    """
    Mengambil riwayat data kualitas air terbaru dari Data-Service.
    """
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(
            f"{DATA_SERVICE_URL}/data/samples/latest",
            params={"limit": limit}
        )
        response.raise_for_status()
        return response.json()
