# services/api-service/tests/conftest.py
# Shared fixtures untuk semua test di api-service

VALID_PAYLOAD = {
    "temperature": 28.5,
    "turbidity": 15.0,
    "dissolved_oxygen": 6.5,
    "bod": 3.0,
    "co2": 5.0,
    "ph": 7.2,
    "alkalinity": 120.0,
    "hardness": 80.0,
    "calcium": 40.0,
    "ammonia": 0.02,
    "nitrite": 0.01,
    "phosphorus": 0.5,
    "h2s": 0.001,
    "plankton_count": 5000.0,
}

MOCK_ML_RESPONSE = {
    "prediction": "Optimal Suitability",
    "confidence": 0.95
}

MOCK_DB_RESPONSE = {
    "status": "success",
    "data": [{**VALID_PAYLOAD, "prediction_tier": "Optimal Suitability"}]
}

MOCK_HISTORY_RESPONSE = [
    {**VALID_PAYLOAD, "id": 1, "prediction_tier": "Optimal Suitability", "created_at": "2026-05-15T00:00:00"}
]
