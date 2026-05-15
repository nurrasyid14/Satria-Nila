# services/ml-service/app/core/mlflow_tracking.py
# INFRASTRUCTURE: Abstraksi untuk logging eksperimen ke MLflow Tracking Server
# Status: PLACEHOLDER — akan diimplementasikan saat transisi MLOps (Tahap 3)

"""
Modul ini akan berisi fungsi untuk mencatat parameter, metrik, 
dan artifact model ke MLflow Tracking Server.

Contoh penggunaan (masa depan):
    log_experiment(params={"n_estimators": 100}, metrics={"f1": 0.95})
"""


def log_experiment(params: dict = None, metrics: dict = None):
    """
    Placeholder: Mencatat hasil eksperimen ke MLflow.
    """
    raise NotImplementedError(
        "MLflow Tracking Server belum dikonfigurasi. "
        "Logging eksperimen belum tersedia."
    )
