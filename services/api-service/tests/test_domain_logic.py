# services/api-service/tests/test_domain_logic.py
# TDD: Unit Tests untuk Domain Layer API Service
# Referensi: tdd_strategy.md — Test Cases API-U01 ~ API-U05

import pytest
from pydantic import ValidationError
from app.schemas.water_schema import WaterQualityInput
from app.domain.water_logic import get_tier_recommendation
from tests.conftest import VALID_PAYLOAD


# --- API-U01: Schema menerima 14 field valid ---
def test_valid_input_accepted():
    """WaterQualityInput harus menerima payload lengkap tanpa error."""
    data = WaterQualityInput(**VALID_PAYLOAD)
    assert data.ph == 7.2
    assert data.temperature == 28.5


# --- API-U02: Schema menolak field non-numerik ---
def test_non_numeric_rejected():
    """Field dengan tipe non-numerik (string) harus ditolak oleh Pydantic."""
    invalid = {**VALID_PAYLOAD, "temperature": "hangat"}
    with pytest.raises(ValidationError):
        WaterQualityInput(**invalid)


# --- API-U03: Schema menolak field yang hilang ---
def test_missing_field_rejected():
    """Payload tanpa salah satu field wajib harus ditolak."""
    incomplete = {k: v for k, v in VALID_PAYLOAD.items() if k != "temperature"}
    with pytest.raises(ValidationError):
        WaterQualityInput(**incomplete)


# --- API-U04: get_tier_recommendation mengembalikan rekomendasi untuk semua tier ---
def test_all_tiers_have_recommendations():
    """Setiap tier yang dikenali harus mengembalikan description dan recommendation."""
    for tier in ["Optimal Suitability", "Moderate Suitability", "Reduced Suitability"]:
        result = get_tier_recommendation(tier)
        assert "description" in result, f"Tier '{tier}' tidak punya description"
        assert "recommendation" in result, f"Tier '{tier}' tidak punya recommendation"
        assert len(result["recommendation"]) > 0, f"Tier '{tier}' recommendation kosong"


# --- API-U05: Tier tidak dikenal mengembalikan fallback ---
def test_unknown_tier_returns_fallback():
    """Tier yang tidak dikenali harus mengembalikan pesan fallback."""
    result = get_tier_recommendation("99")
    assert "administrator" in result["recommendation"].lower()
