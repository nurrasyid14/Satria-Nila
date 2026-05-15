# services/data-service/tests/test_water_routes.py
# TDD: Unit Tests untuk Data Service Water Quality Routes
# Referensi: tdd_strategy.md — Test Cases DS-U01 ~ DS-U04
# Menggunakan mock untuk Supabase agar test berjalan tanpa koneksi internet.

import os
import sys
import pytest
from unittest.mock import MagicMock

# --- Set env vars SEBELUM import apapun dari app ---
os.environ["SUPABASE_URL"] = "https://mock.supabase.co"
os.environ["SUPABASE_KEY"] = "mock-key-for-testing"

# --- Mock library supabase jika tidak terinstall ---
_mock_client = MagicMock()
_mock_response = MagicMock()
_mock_response.data = [{"id": 1, "temperature": 28.5, "prediction_tier": "Optimal Suitability"}]

_mock_client.table.return_value.insert.return_value.execute.return_value = _mock_response
_mock_client.table.return_value.select.return_value.order.return_value.limit.return_value.execute.return_value = _mock_response
_mock_client.table.return_value.select.return_value.order.return_value.range.return_value.execute.return_value = _mock_response

# Inject mock supabase module ke sys.modules
mock_supabase_lib = MagicMock()
mock_supabase_lib.create_client.return_value = _mock_client
mock_supabase_lib.Client = type("Client", (), {})
sys.modules.setdefault("supabase", mock_supabase_lib)

# Sekarang aman untuk import app
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# --- Fixture: Data payload valid ---
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
    "prediction_tier": "Optimal Suitability",
}


# --- DS-U01: App berhasil diinisialisasi ---
def test_app_initialized():
    """App dan semua dependency berhasil dimuat tanpa error."""
    assert app is not None
    assert client is not None


# --- DS-U02: POST /data/samples mengembalikan 201 ---
def test_insert_sample_returns_201():
    """Endpoint insert harus mengembalikan 201 Created dengan payload valid."""
    response = client.post("/data/samples", json=VALID_PAYLOAD)
    assert response.status_code == 201, (
        f"Expected 201, got {response.status_code}: {response.text}"
    )
    data = response.json()
    assert data["status"] == "success"
    assert "data" in data


# --- DS-U03: GET /data/samples/latest mengembalikan list ---
def test_get_latest_returns_list():
    """Endpoint latest harus mengembalikan list data."""
    response = client.get("/data/samples/latest")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


# --- DS-U04: POST dengan body tidak lengkap mengembalikan 422 ---
def test_incomplete_body_returns_422():
    """Request dengan body tidak lengkap harus ditolak dengan 422."""
    incomplete = {"temperature": 28.5, "ph": 7.2}
    response = client.post("/data/samples", json=incomplete)
    assert response.status_code == 422
