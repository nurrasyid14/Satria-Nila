# services/api-service/tests/test_predict_flow.py
# TDD: Integration Tests untuk alur prediksi end-to-end
# Referensi: tdd_strategy.md — Test Cases INT-01 ~ INT-05
# Semua external calls (ML-Service, Data-Service) di-mock.
# PENTING: Mock harus di-patch di lokasi dimana fungsi DIGUNAKAN (routes/water.py),
# bukan di lokasi dimana fungsi DIDEFINISIKAN (clients/).

import pytest
from unittest.mock import AsyncMock, patch
from fastapi.testclient import TestClient
from app.main import app
from tests.conftest import VALID_PAYLOAD, MOCK_ML_RESPONSE, MOCK_HISTORY_RESPONSE

client = TestClient(app)

# Path mock harus mengarah ke module yang MENGGUNAKAN fungsi tersebut
ML_MOCK_PATH = "app.routes.water.call_ml_service"
SAVE_MOCK_PATH = "app.routes.water.save_to_database"
HISTORY_MOCK_PATH = "app.routes.water.get_latest_data"


# --- INT-01: POST /predict mengembalikan 200 + prediction_tier ---
@patch(SAVE_MOCK_PATH, new_callable=AsyncMock)
@patch(ML_MOCK_PATH, new_callable=AsyncMock)
def test_predict_returns_valid_response(mock_ml, mock_save):
    """Alur prediksi lengkap harus mengembalikan 200 dengan response yang valid."""
    mock_ml.return_value = MOCK_ML_RESPONSE
    mock_save.return_value = {"status": "success"}

    response = client.post("/api/v1/water-quality/predict", json=VALID_PAYLOAD)

    assert response.status_code == 200, f"Got {response.status_code}: {response.text}"
    data = response.json()
    assert data["prediction_tier"] == "Optimal Suitability"
    assert data["confidence"] == 0.95


# --- INT-02: Response menyertakan recommendation ---
@patch(SAVE_MOCK_PATH, new_callable=AsyncMock)
@patch(ML_MOCK_PATH, new_callable=AsyncMock)
def test_predict_includes_recommendation(mock_ml, mock_save):
    """Response prediksi harus menyertakan recommendation dari domain layer."""
    mock_ml.return_value = MOCK_ML_RESPONSE
    mock_save.return_value = {"status": "success"}

    response = client.post("/api/v1/water-quality/predict", json=VALID_PAYLOAD)

    data = response.json()
    assert "recommendation" in data
    assert len(data["recommendation"]) > 0


# --- INT-03: GET /history mengembalikan 200 + list ---
@patch(HISTORY_MOCK_PATH, new_callable=AsyncMock)
def test_history_returns_list(mock_get):
    """Endpoint history harus mengembalikan status 200 dengan data berupa list."""
    mock_get.return_value = MOCK_HISTORY_RESPONSE

    response = client.get("/api/v1/water-quality/history")

    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)


# --- INT-04: ML-Service down → 502 ---
@patch(ML_MOCK_PATH, new_callable=AsyncMock)
def test_ml_service_down_returns_502(mock_ml):
    """Jika ML-Service gagal, API harus mengembalikan 502 Bad Gateway."""
    mock_ml.side_effect = Exception("Connection refused")

    response = client.post("/api/v1/water-quality/predict", json=VALID_PAYLOAD)

    assert response.status_code == 502


# --- INT-05: Data-Service down → prediksi tetap 200 (graceful degradation) ---
@patch(SAVE_MOCK_PATH, new_callable=AsyncMock)
@patch(ML_MOCK_PATH, new_callable=AsyncMock)
def test_data_service_down_still_returns_prediction(mock_ml, mock_save):
    """Jika Data-Service gagal, prediksi tetap dikembalikan (graceful degradation)."""
    mock_ml.return_value = MOCK_ML_RESPONSE
    mock_save.side_effect = Exception("Data-Service unreachable")

    response = client.post("/api/v1/water-quality/predict", json=VALID_PAYLOAD)

    assert response.status_code == 200
    data = response.json()
    assert data["prediction_tier"] == "Optimal Suitability"
