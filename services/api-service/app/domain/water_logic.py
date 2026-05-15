# services/api-service/app/domain/water_logic.py
# DOMAIN LAYER: Logika bisnis untuk penilaian kualitas air
# Dipindahkan dari schemas/prediction_schema.py agar schema tetap murni definisi data.

# Mapping deskripsi dan rekomendasi berdasarkan tier prediksi ML
TIER_INFO = {
    "Optimal Suitability": {
        "description": "Kualitas air sangat baik dan ideal untuk budidaya ikan nila.",
        "recommendation": "Pertahankan kondisi saat ini. Lakukan monitoring rutin setiap 6 jam."
    },
    "Optimal": {
        "description": "Kualitas air sangat baik dan ideal untuk budidaya ikan nila.",
        "recommendation": "Pertahankan kondisi saat ini. Lakukan monitoring rutin setiap 6 jam."
    },
    "Moderate Suitability": {
        "description": "Kualitas air cukup baik, namun beberapa parameter perlu perhatian.",
        "recommendation": (
            "Periksa parameter yang mendekati ambang batas. "
            "Tingkatkan frekuensi monitoring menjadi setiap 3 jam."
        )
    },
    "Reduced Suitability": {
        "description": "Kualitas air kurang ideal. Terdapat parameter yang melebihi ambang batas aman.",
        "recommendation": (
            "SEGERA lakukan tindakan koreksi. Periksa aerasi, "
            "lakukan pergantian air parsial, dan cek sumber kontaminan."
        )
    }
}

# Fallback untuk tier yang tidak dikenali
_FALLBACK = {
    "description": "Tier prediksi tidak dikenali oleh sistem.",
    "recommendation": "Silakan hubungi administrator sistem untuk verifikasi hasil."
}


def get_tier_recommendation(prediction_label: str) -> dict:
    """
    Mengembalikan deskripsi dan rekomendasi aksi berdasarkan label tier.

    Args:
        prediction_label: Label dari ML-Service (contoh: "Optimal Suitability")

    Returns:
        dict berisi 'description' dan 'recommendation'.
    """
    return TIER_INFO.get(prediction_label, _FALLBACK)
