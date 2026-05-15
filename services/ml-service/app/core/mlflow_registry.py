# services/ml-service/app/core/mlflow_registry.py
# INFRASTRUCTURE: Abstraksi untuk pengambilan model dari MLflow Model Registry
# Status: PLACEHOLDER — akan diimplementasikan saat transisi MLOps (Tahap 3)

"""
Modul ini akan berisi fungsi untuk mengunduh model terbaru dari MLflow
Model Registry berdasarkan stage (Staging/Production).

Contoh penggunaan (masa depan):
    model_uri = "models:/SatriaNilaWater/Production"
    model = load_model_from_registry(model_uri)
"""


def load_model_from_registry(model_name: str, stage: str = "Production"):
    """
    Placeholder: Mengunduh model dari MLflow Registry.
    Akan menggantikan pemuatan model lokal dari artifacts/ di production.
    """
    raise NotImplementedError(
        f"MLflow Registry belum dikonfigurasi. "
        f"Model '{model_name}' stage '{stage}' tidak dapat dimuat. "
        f"Gunakan local artifacts untuk saat ini."
    )
