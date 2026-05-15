# services/api-service/app/routes/health.py

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    """Cek status API-Service."""
    return {"status": "online", "service": "api-service"}
