# services/ml-service/tests/test_water_predict.py
# TDD: Unit Tests untuk Domain Water Quality Inference
# Referensi: tdd_strategy.md — Test Cases ML-U01 ~ ML-U05

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.domains.water.predict import get_prediction

client = TestClient(app)

# --- Fixture: Data input valid (14 parameter) ---
VALID_INPUT = {
    "Temperature": 28.5,
    "Turbidity (cm)": 15.0,
    "Dissolved Oxygen (mg/L)": 6.5,
    "Biochemical Oxygen Demand (mg/L)": 3.0,
    "Carbon Dioxide (CO2)": 5.0,
    "pH": 7.2,
    "Total Alkalinity (mg L-1)": 120.0,
    "Total Hardness (mg L-1)": 80.0,
    "Calcium (mg L-1)": 40.0,
    "Ammonia (mg L-1)": 0.02,
    "Nitrite (mg L-1)": 0.01,
    "Phosphorus (mg L-1)": 0.5,
    "Hydrogen Sulfide (mg L-1)": 0.001,
    "Plankton Count (No. L-1)": 5000.0,
}

VALID_API_PAYLOAD = {
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

VALID_LABELS = {"Optimal Suitability", "Moderate Suitability", "Reduced Suitability"}


# --- ML-U01: Model berhasil dimuat ke memori ---
def test_model_loaded():
    """Model PyCaret harus berhasil dimuat saat modul di-import."""
    from app.domains.water.predict import model
    assert model is not None, "Model gagal dimuat — periksa path artifacts/"


# --- ML-U02: Prediksi mengembalikan label valid ---
def test_prediction_returns_valid_label():
    """Hasil prediksi harus salah satu dari 3 label yang dikenali sistem."""
    result = get_prediction(VALID_INPUT)
    assert result["prediction"] in VALID_LABELS, (
        f"Label '{result['prediction']}' tidak termasuk dalam {VALID_LABELS}"
    )


# --- ML-U03: Confidence berada di range 0-1 ---
def test_confidence_in_range():
    """Skor confidence harus berada di antara 0.0 dan 1.0."""
    result = get_prediction(VALID_INPUT)
    assert 0.0 <= result["confidence"] <= 1.0, (
        f"Confidence {result['confidence']} di luar rentang [0, 1]"
    )


# --- ML-U04: Input tidak lengkap menghasilkan error ---
def test_incomplete_input_raises_error():
    """Input dengan kolom yang kurang harus menghasilkan Exception."""
    incomplete = {"Temperature": 28.5, "pH": 7.2}  # Hanya 2 dari 14
    with pytest.raises(Exception):
        get_prediction(incomplete)


# --- ML-U05: Endpoint /predict/water mengembalikan 200 OK ---
def test_predict_endpoint_returns_200():
    """Endpoint API harus mengembalikan status 200 dengan payload valid."""
    response = client.post("/predict/water", json=VALID_API_PAYLOAD)
    assert response.status_code == 200, (
        f"Expected 200, got {response.status_code}: {response.text}"
    )
    data = response.json()
    assert "prediction" in data
    assert "confidence" in data
