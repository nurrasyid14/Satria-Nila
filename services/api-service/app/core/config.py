# services/api-service/app/core/config.py
# INFRASTRUCTURE: Sentralisasi konfigurasi environment variables
# Memperbaiki pencarian .env agar lebih robust

import os
from dotenv import load_dotenv


def _find_and_load_env():
    """Mencari file .env di lokasi yang mungkin dan memuatnya."""
    base = os.path.dirname(__file__)
    candidates = [
        os.path.join(base, '..', '..', '..', '.env'),       # services/.env
        os.path.join(base, '..', '..', '..', '..', '.env'),  # root .env
    ]
    for path in candidates:
        abs_path = os.path.abspath(path)
        if os.path.exists(abs_path):
            load_dotenv(dotenv_path=abs_path, override=True)
            return abs_path
    return None


_find_and_load_env()

# URL ke microservice lain (default untuk development lokal)
ML_SERVICE_URL = os.getenv("ML_SERVICE_URL", "http://127.0.0.1:8001")
DATA_SERVICE_URL = os.getenv("DATA_SERVICE_URL", "http://127.0.0.1:8002")
