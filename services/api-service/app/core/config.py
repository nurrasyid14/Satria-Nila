# services/api-service/app/core/config.py

import os
from dotenv import load_dotenv

# Memuat .env dari root proyek (naik 3 tingkat dari app/core/)
env_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '.env')
load_dotenv(dotenv_path=env_path)

# URL ke microservice lain (default untuk development lokal)
ML_SERVICE_URL = os.getenv("ML_SERVICE_URL", "http://127.0.0.1:8001")
DATA_SERVICE_URL = os.getenv("DATA_SERVICE_URL", "http://127.0.0.1:8002")
